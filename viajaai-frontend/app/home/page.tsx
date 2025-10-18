"use client";
import React, { useState } from "react";
import { Star, User } from "lucide-react";
import { useUser } from "../../context/UserContext";
import { useRouter } from "next/navigation";

interface Destino {
  viagem_id: number;
  score: number;
  img?: string;
  nome?: string;
  custo?: string;
  rating?: number;
  descricao?:string
}

export default function HomePage() {
  const [destinos, setDestinos] = useState<Destino[]>([]);
  const { user } = useUser();
  const router = useRouter();


  const handleComprar = async (e:React.FormEvent,viagem_id:number) => {
    e.preventDefault();
    if (!user){
      alert("Usuário não logado!");
      return;
    }
    try{

      const res = await fetch("http://localhost:5000/api/viagem/comprar",{
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ userId: user.Id, viagemId: viagem_id }),
      })

      const data = await res.json();
      if (data.ok){
        alert("Viagem comprada com sucesso!")
        router.push('/viagem')
      }
      else{
        alert(data.error || "Erro ao comprar viagem.");
      }
      

      if (!res.ok) {
        throw new Error(`Erro ao comprar viagens: ${res.status}`);
      }

    }
    catch(error){
      console.error("Erro:", error);
      alert("Erro ao buscar viagens");
    }
  }

  const handleRecomendar = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!user) {
      alert("Usuário não logado!");
      return;
    }

    try {
      const res = await fetch("http://localhost:5000/api/recomendacao/recomendar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: user.Id }), 
      });

      if (!res.ok) {
        throw new Error(`Erro ao recomendar viagens: ${res.status}`);
      }

      const data = await res.json();
      
      if (data.ok) {
        setDestinos(data.recomendacoes);
      } else {
        alert(data.error);
      }
    } catch (error) {
      console.error("Erro:", error);
      alert("Erro ao buscar recomendações");
    }
  };

  return (
    <div className="min-h-screen flex flex-col font-sans bg-white">
      {/* Header */}
      <header className="flex justify-between items-center px-10 py-4 bg-white shadow-sm">
        <div className="flex items-center space-x-2">
          <div 
            className="bg-white text-white rounded-full p-2 h-15 w-15" 
            style={{ backgroundImage: "url('/icon.png')" }}
          ></div>
          <h1 className="text-lg font-semibold text-blue-700">Viaja.AI</h1>
        </div>
        <nav className="flex space-x-8 text-gray-700 md:text-2xl">
          <a href="/home" className="hover:text-blue-600">Home</a>
          <a href="/viagem" className="hover:text-blue-600">Viagens</a>
        </nav>
        <div className="flex items-center gap-2">
          <span className="text-blue-700 md:text-2xl">{user?.Nome}</span>
          <div className="bg-gray-300 rounded-full p-2">
            <User size={18}/>
          </div>
        </div>
      </header>

      <section
        className="relative w-full h-120 bg-cover bg-center flex items-center justify-center "
        style={{ backgroundImage: "url('/home.png')" }}
      >
        <div className="text-center">
          <h2 className="text-2xl md:text-5xl font-semibold text-blue-800 px-15 py-2 rounded">
            Sua próxima viagem
          </h2>
          <h2 className="text-2xl md:text-5xl font-semibold text-blue-800 px-45 py-2 rounded">
            começa aqui.
          </h2>
          
          {/* Botão para buscar recomendações */}
          <button 
            onClick={handleRecomendar}
            className="mt-6 bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700 transition"
          >
            Ver Minhas Recomendações
          </button>
        </div>
      </section>

      {/* Seção de sugestões */}
      <main className="flex flex-col items-center mt-15 px-6 bg-white">
        <div className="flex justify-between items-center w-full max-w-6xl mb-6">
          <h2 className="text-2xl font-bold text-gray-800 md:text-3xl">
            {destinos.length > 0 ? "Suas recomendações" : "Confira as nossas sugestões de viagens para você"}
          </h2>
          <button className="text-white px-6 py-2 rounded-2xl hover:shadow-lg transition overflow-hidden" style={{ backgroundColor: "#45736A" }}>
            Filtrar
          </button>
        </div>

        {/* Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mt-15">
          {destinos.length > 0 ? (
            destinos.map((d, i) => (
              <div key={i} className="bg-green-100 rounded-2xl shadow hover:shadow-lg transition overflow-hidden">
                <img 
                  src={d.img || "/placeholder.jpg"} 
                  alt={d.nome || `Viagem ${d.viagem_id}`} 
                  className="w-full h-44 object-cover" 
                />
                <div className="p-4">
                  <h3 className="text-lg font-bold text-gray-500 mb-2">
                    {d.nome || `Viagem ${d.viagem_id}`}
                  </h3>
                  <p className="text-sm text-gray-500">{d.descricao}</p>
                  <p className="text-sm text-gray-700">Similaridade: {d.score.toFixed(2)}</p>
                  {d.custo && <p className="text-sm text-green-700">Custo: {d.custo}</p>}
                  <div className="flex mt-2">
                    {[...Array(5)].map((_, j) => (
                      <Star
                        key={j}
                        size={16}
                        className={j < (d.rating || 0) ? "text-yellow-400" : "text-gray-300"}
                        fill={j < (d.rating || 0) ? "yellow" : "none"}
                      />
                    ))}
                  </div>
                  <div >
                    <button 
                    onClick={(e)=>handleComprar(e,d.viagem_id)}
                    className="bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700 transition">
                      Comprar
                      </button>
                  </div>
                </div>
              </div>
            ))
          ) : (
            <p className="text-gray-500 col-span-3 text-center py-8">
              Clique em "Ver Minhas Recomendações" para ver sugestões personalizadas
            </p>
          )}
        </div>
      </main>

      {/* Rodapé */}
      <footer className="mt-12 relative h-80" style={{ backgroundColor: "#45736A" }}>
        <div
          className="h-full w-full bg-no-repeat bg-cover bg-top"
          style={{ backgroundImage: "url('/wave-footer.png')" }}
        ></div>
      </footer>
    </div>
  );
}
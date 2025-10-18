"use client";
import React, { useState, useEffect } from "react";
import { Star, User } from "lucide-react";
import { useUser } from "../../context/UserContext";

interface Destino {
  viagem_id: number;
  img?: string;
  nome?: string;
  custo?: string;
  rating?: number;
  descricao?: string;
}

export default function Viagem() {
  const [destinos, setDestinos] = useState<Destino[]>([]);
  const { user } = useUser();
  const [pontuacaoAtual, setPontuacaoAtual] = useState<{ [key: number]: number }>(
    {}
  );

  useEffect(() => {
    if (user) {
      handleObterViagens();
    }
  }, [user]);

  const handleAvaliar = async (viagem_id: number, pontuacao: number) => {
    if (!user) {
      alert("Usuário não logado!");
      return;
    }

    try {
      const res = await fetch("http://localhost:5000/api/viagem/avaliar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ userId: user.Id, viagemId: viagem_id, pontuacao }),
      });

      const data = await res.json();
      if (data.ok) {
        // Atualiza localmente o rating no estado
        setDestinos((prev) =>
          prev.map((d) =>
            d.viagem_id === viagem_id ? { ...d, rating: pontuacao } : d
          )
        );
        setPontuacaoAtual((prev) => ({ ...prev, [viagem_id]: pontuacao }));
      } else {
        alert(data.error || "Erro ao avaliar viagem.");
      }
    } catch (error) {
      console.error("Erro:", error);
      alert("Erro ao avaliar viagem");
    }
  };

  const handleObterViagens = async () => {
    if (!user) return;

    try {
      const res = await fetch("http://localhost:5000/api/viagem/obter", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ userId: user.Id }),
      });

      if (!res.ok) throw new Error(`Erro ao obter viagens: ${res.status}`);

      const data = await res.json();
      if (data.ok) {
        const viagensFormatadas = data.viagens.map((v: any) => ({
          viagem_id: v.Id,
          nome: v.Nome,
          descricao: v.Descricao,
          custo: v.Preco,
          rating: v.Avaliacao,
          img: v.img || "/placeholder.jpg",
        }));
        setDestinos(viagensFormatadas);

        // Inicializa pontuaçãoAtual com as avaliações existentes
        const initialRatings: { [key: number]: number } = {};
        viagensFormatadas.forEach((v) => {
          initialRatings[v.viagem_id] = v.rating || 0;
        });
        setPontuacaoAtual(initialRatings);
      } else {
        alert(data.error);
      }
    } catch (error) {
      console.error("Erro:", error);
      alert("Erro ao buscar viagens do usuario");
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
          <a href="/home" className="hover:text-blue-600">
            Home
          </a>
          <a href="/viagem" className="hover:text-blue-600">
            Viagens
          </a>
        </nav>
        <div className="flex items-center gap-2">
          <span className="text-blue-700 md:text-2xl">{user?.Nome}</span>
          <div className="bg-gray-300 rounded-full p-2">
            <User size={18} />
          </div>
        </div>
      </header>

      <main className="flex flex-col items-center mt-15 px-6 bg-white">
        <div className="flex justify-between items-center w-full max-w-6xl mb-6">
          <h2 className="text-2xl font-bold text-gray-800 md:text-3xl">
            {destinos.length > 0
              ? "Suas viagens"
              : "Confira as nossas sugestões de viagens para você"}
          </h2>
          <button
            className="text-white px-6 py-2 rounded-2xl hover:shadow-lg transition overflow-hidden"
            style={{ backgroundColor: "#45736A" }}
          >
            Filtrar
          </button>
        </div>

        {/* Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mt-15">
          {destinos.length > 0 ? (
            destinos.map((d) => (
              <div
                key={d.viagem_id}
                className="bg-green-100 rounded-2xl shadow hover:shadow-lg transition overflow-hidden"
              >
                <img
                  src={d.img}
                  alt={d.nome || `Viagem ${d.viagem_id}`}
                  className="w-full h-44 object-cover"
                />
                <div className="p-4">
                  <h3 className="text-lg font-bold text-gray-500 mb-2">
                    {d.nome || `Viagem ${d.viagem_id}`}
                  </h3>
                  <p className="text-sm text-gray-500">{d.descricao}</p>
                  {d.custo && (
                    <p className="text-sm text-green-700">Custo: {d.custo}</p>
                  )}
                  <div className="flex mt-2 mb-2">
                    {[1, 2, 3, 4, 5].map((n) => (
                      <Star
                        key={n}
                        size={24}
                        className={
                          n <= (pontuacaoAtual[d.viagem_id] || 0)
                            ? "text-yellow-400 cursor-pointer"
                            : "text-gray-300 cursor-pointer"
                        }
                        fill={n <= (pontuacaoAtual[d.viagem_id] || 0) ? "yellow" : "none"}
                        onClick={() => handleAvaliar(d.viagem_id, n)}
                      />
                    ))}
                  </div>
                </div>
              </div>
            ))
          ) : (
            <p className="text-gray-500 col-span-3 text-center py-8">
              Vá para pagina inicial e veja nossas recomendações para você!
            </p>
          )}
        </div>
      </main>

      {/* Rodapé */}
      <footer
        className="mt-12 relative h-80"
        style={{ backgroundColor: "#45736A" }}
      >
        <div
          className="h-full w-full bg-no-repeat bg-cover bg-top"
          style={{ backgroundImage: "url('/wave-footer.png')" }}
        ></div>
      </footer>
    </div>
  );
}

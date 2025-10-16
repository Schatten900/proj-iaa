"use client";

import { useState } from "react";
import { useRouter } from 'next/navigation'
import { useUser } from "../../context/UserContext";

type Opcao = {
  id: string;
  titulo: string;
  descricao: string;
};

export default function Preferencias() {
  const opcoes: Opcao[] = [
    { id: "1", titulo: "Romance", descricao: "Viagens românticas para casais" },
    { id: "2", titulo: "Aventura", descricao: "Viagens com atividades emocionantes e radicais" },
    { id: "3", titulo: "Relaxamento", descricao: "Viagens focadas em descanso e bem-estar" },
    { id: "4", titulo: "Histórico", descricao: "Viagens com foco em patrimônio histórico" },
    { id: "5", titulo: "Cultural", descricao: "Viagens para experienciar diferentes culturas" },
    { id: "6", titulo: "Gastronômico", descricao: "Viagens focadas em experiências culinárias" },
    { id: "7", titulo: "Ecoturismo", descricao: "Viagens de contato com a natureza" },
  ];

  const [selecionados, setSelecionados] = useState<{ [key: string]: number }>({});
  const { user } = useUser();
  const router = useRouter()

  const toggleOpcao = (id: string) => {
    setSelecionados((prev) => {
      const newSelection = { ...prev };
      if (newSelection[id] !== undefined) {
        delete newSelection[id];
      } else {
        newSelection[id] = 1;
      }
      return newSelection;
    });
  };

  const [hover, setHover] = useState(false);

  const handleIntensityChange = ( id: number, intensity: number) => {
    setSelecionados((prev) => {
      if (prev[id] !== undefined && user !== undefined) {
        return { ...prev, [id]: intensity };
      }
      return prev;
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!user) {
            alert("Usuário não logado!");
            return;
    }

    console.log(selecionados)

    for (const [ id, Preferencia] of Object.entries(selecionados)) {
      const res = await fetch("http://localhost:5000/api/viagem/generos", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          UsuarioId: user.Id,
          GeneroId: id, 
          Preferencia }),
      });
    
      if (!res.ok) {
        alert(`Erro ao cadastrar o gênero ${id}`);
        return;
      }
    }
    
    alert("Gêneros cadastrados com sucesso!");
    router.push('/home');
  };

  return (
    <div
      className="flex flex-col items-center justify-center min-h-screen bg-cover bg-center px-4"
      style={{ backgroundImage: "url('/aviao.png')" }}
    >
      {/* Título */}
      <div className="text-center text-white mb-8">
         <h1 style={{ fontSize: "3.5rem", fontWeight: "bold", marginBottom: "1rem", textShadow: "2px 2px 4px rgba(0,0,0,0.7)"}}>
                Está sendo ótimo te conhecer, {user?.Nome}!
            </h1>
            <h2 style={{ fontSize: "2rem", marginBottom: "2rem", textShadow: "2px 2px 4px rgba(0,0,0,0.7)"}}>
                Qual o seu gênero de viagem preferido?
            </h2>
      </div>

      {/* Card central */}
      <div className="bg-white/40 rounded-4xl p-8 shadow-lg max-w-2xl w-full">
        {/* Grid de opções */}
        <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
          {opcoes.map((opcao) => {
            const selecionado = selecionados.hasOwnProperty(opcao.id);
            return (
              <label
                key={opcao.id}
                onClick={() => toggleOpcao(opcao.id)}
                className={`cursor-pointer rounded-xl p-4 text-center transition-all duration-200 border 
                ${selecionado
                  ? "bg-[#45736A] text-white shadow-md border-[#45736A]"
                  : "bg-[#D3E1DC] text-gray-800 hover:bg-[#C0D5CE] border-transparent"
                }`}
              >
                <input
                  type="checkbox"
                  checked={selecionado}
                  onChange={() => toggleOpcao(opcao.id)}
                  className="hidden"
                />
                <p className="font-semibold">{opcao.titulo}</p>
                <p className="text-sm">{opcao.descricao}</p>
                <select style={{ backgroundColor: "#45736A" }}>
                    <option value="1" style={{ color: "black" }}>1</option>
                    <option value="2" style={{ color: "black" }}>2</option>
                    <option value="3" style={{ color: "black" }}>3</option>
                    <option value="4" style={{ color: "black" }}>4</option>
                    <option value="5" style={{ color: "black" }}>5</option>
                </select>
              </label>
            );
          })}
        </div>
      </div>

      {/*Botão avançar*/}
            <button
                type="submit"
                onClick={handleSubmit}
                onMouseEnter={() => setHover(true)}
                onMouseLeave={() => setHover(false)}
                style={{
                    position: "fixed",
                    bottom: "20px",
                    right: "20px",
                    marginTop: "2rem",
                    background: hover ? "#D9E6E6": "#F2EFEF" ,
                    color: "#000",
                    borderRadius: "50%",
                    width: "80px",
                    height: "40px",
                    padding: "15px",
                    border: "none",
                    cursor: "pointer",
                    fontSize: "1.2rem",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                }}
            >
                ➡
            </button>
    </div>

    
  );
  
    console.log(selecionados)
}

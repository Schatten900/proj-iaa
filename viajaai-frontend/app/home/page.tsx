import React from "react";
import { Star, User } from "lucide-react";

export default function HomePage(){
    const destinos = [
        { nome: "Acapulco", pais: "México", custo: "R$ XX,XX", moeda: "R$ XX,XX", img: '/acapulco.png', rating: 4 }, 
        { nome: "Lençóis Maranhenses", pais: "Brasil", custo: "R$ XX,XX", moeda: "R$ XX,XX", img: '/maranhao.png', rating: 5 }, 
        { nome: "Rio de Janeiro", pais: "Brasil", custo: "R$ XX,XX", moeda: "R$ XX,XX", img: '/rio.png', rating: 5 }, 
    ];

    return (
        <div className="min-h-screen flex flex-col font-sans">
            {/* Header */}
            <header className="flex justify-between items-center px-10 py-4 bg-white shadow-sm">
                <div className="flex items-center space-x-2">
                    <div className="bg-white text-white rounded-full p-2 h-15 w-15" style={{ backgroundImage: "url('/icon.png')" }}></div>
                    <h1 className="text-lg font-semibold text-blue-700">Viaja.AI</h1>
                </div>
                <nav className="flex space-x-8 text-gray-700 md:text-2xl">
                    <a href="#" className="hover:text-blue-600">Home</a>
                    <a href="#" className="hover:text-blue-600">Viagens</a>
                    <a href="#" className="hover:text-blue-600">Sobre</a>
                    <a href="#" className="hover:text-blue-600">Contato</a>
                </nav>
                <div className="flex items-center gap-2">
                    <span className="text-blue-700 md:text-2xl">User</span>
                    <div className="bg-gray-300 rounded-full p-2">
                        <User size={18}/>
                    </div>
                </div>
            </header>

            <section
                className="relative w-full h-120 bg-cover bg-center flex items-center justify-center"
                style={{ backgroundImage: "url('/home.png')" }}
            >
                <h2 className="text-2xl md:text-5xl font-semibold text-blue-800 px-15 py-2 rounded">
                    Sua próxima viagem
                </h2>

                <h2 className="text-2xl md:text-5xl font-semibold text-blue-800 px-45 py-2 rounded">
                    começa aqui.
                </h2>
            </section>

            {/* Seção de sugestões */}
            <main className="flex flex-col items-center mt-15 px-6">
                <div className="flex justify-between items-center w-full max-w-6xl mb-6">
                <h2 className="text-2xl font-bold text-gray-800 md:text-3xl">
                    Confira as nossas sugestões de viagens para você
                </h2>
                <button className="text-white px-6 py-2 rounded-2xl hover:shadow-lg transition overflow-hidden" style={{ backgroundColor: "#45736A" }}>
                    Filtrar
                </button>
                </div>

                {/* Cards */}
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mt-15">
                {destinos.map((d, i) => (
                    <div key={i} className="bg-green-100 rounded-2xl shadow hover:shadow-lg transition overflow-hidden">
                    <img src={d.img} alt={d.nome} className="w-full h-44 object-cover" />
                    <div className="p-4">
                        <h3 className="text-lg font-semibold mb-2">{d.nome}</h3>
                        <p className="text-sm text-gray-700">País: {d.pais}</p>
                        <p className="text-sm text-gray-700">Custo em média: {d.custo}</p>
                        <p className="text-sm text-gray-700">Valor da moeda: {d.moeda}</p>
                        <div className="flex mt-2">
                        {[...Array(5)].map((_, j) => (
                            <Star
                            key={j}
                            size={16}
                            className={j < d.rating ? "text-yellow-400" : "text-gray-300"}
                            fill={j < d.rating ? "yellow" : "none"}
                            />
                        ))}
                        </div>
                    </div>
                    </div>
                ))}
                </div>
            </main>

            {/* Rodapé decorativo */}
            <footer className="mt-12 relative h-80"  style={{ backgroundColor: "#45736A" }}>
                {/* Onda */}
                <div
                    className="h-full w-full bg-no-repeat bg-cover bg-top"
                    style={{ backgroundImage: "url('/wave-footer.png')" }}
                ></div>
            </footer>

        </div>
    );
}




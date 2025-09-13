"use client";
import { useState } from "react";

export default function Perfil() {
    const [form, setForm] = useState({
        orcamento: "",
        duracao: "",
        genero: "",
        pessoas: "",
    });

    const [hover, setHover] = useState(false);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        console.log("Dados do perfil:", form);
        alert("Dados enviados com sucesso!");
    };

    return(
        <div
        style={{
            minHeight: "100vh",
            backgroundImage:"url(/aviao.png)",
            backgroundSize: "cover",
            backgroundPosition: "center",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            padding: "2rem",
            color: "#fff",
        }}
        >
            {/*Cabeçalho*/}

            <h1 style={{ fontSize: "4rem", fontWeight: "bold", marginBottom: "1rem", textShadow: "2px 2px 4px rgba(0,0,0,0.7)"}}>
                Olá, user!
            </h1>
            <h2 style={{ fontSize: "2rem", marginBottom: "2rem", textShadow: "2px 2px 4px rgba(0,0,0,0.7)"}}>
                Nos conte mais sobre você
            </h2>

            {/*Formulário*/}
            <form
                onSubmit={handleSubmit}
                style={{
                    display: "flex",
                    gap: "1rem",
                    flexWrap: "wrap",
                    justifyContent: "center",
                    maxWidth: "1000px",
                }}
            >
            
                {/*Card orçamento*/}
                <div style={cardStyle}>
                    <label style={labelStyle}>Qual seu orçamento para a viagem?</label>
                    <input
                        type="number"
                        name="orcamento"
                        placeholder="R$ 0,00"
                        value="form.orcamento"
                        onChange={handleChange}
                        style={inputStyle}
                    />
                </div>


                {/*Card duração*/}
                <div style={cardStyle}>
                    <label style={labelStyle}>Qual a duração prevista da viagem?</label>
                    <input
                        type="number"
                        name="duracao"
                        placeholder="Escreva em dígitos numéricos"
                        value="form.duracao"
                        onChange={handleChange}
                        style={inputStyle}
                    />
                </div>

                {/*Card gênero*/}
                <div style={cardStyle}>
                    <label style={labelStyle}>Qual o seu<br></br> gênero?</label>
                    <select
                        name="genero"
                        value="form.genero"
                        onChange={handleChange}
                        style={inputStyle}
                    >
                        <option value="Feminino">Feminino</option>
                        <option value="Masculino">Masculino</option>
                        <option value="Outro">Outro</option>
                    </select>
                </div>

                {/*Card pessoas*/}
                <div style={cardStyle}>
                    <label style={labelStyle}>Quantas pessoas irão viajar?</label>
                    <input
                        type="number"
                        name="pessoas"
                        placeholder="Escreva em dígitos numéricos"
                        value="form.pessoas"
                        onChange={handleChange}
                        style={inputStyle}
                    />
                </div>
            </form>

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
    )
}

const cardStyle: React.CSSProperties = {
    background: "#F2EFEF",
    borderRadius: "12px",
    padding: "1rem",
    width: "220px",
    minHeight: "200px",
    textAlign: "center",
    color: "#000",
    boxShadow: "0 4px 12px rgba(0,0,0,0.2)",
};

const labelStyle: React.CSSProperties = {
    display: "block",
    marginBottom: "0.5rem",
    fontWeight: "bold",
};

const inputStyle: React.CSSProperties = {
    width: "100%",
    padding: "10px",
    borderRadius: "10px",
    border: "none",
    background: "#D9E6E6",
    textAlign: "center" as const,
};

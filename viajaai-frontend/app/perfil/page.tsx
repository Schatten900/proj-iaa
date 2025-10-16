"use client";
import { useRouter } from 'next/navigation'
import { useState } from "react";
import { useUser } from "../../context/UserContext";

export default function Perfil() {

    const router = useRouter()
    
    const { user } = useUser();
    const [form, setForm] = useState({
        clima: "Quente",
        preco: "Econômico",
        companhia: "Sozinho",
    });

    const [hover, setHover] = useState(false);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        const { name, value } = e.target;
        setForm({ ...form, [name]: value });
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        if (!user) {
            alert("Usuário não logado!");
            return;
        }
        console.log(form)

        const res = await fetch("http://localhost:5000/api/viagem/preferences", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({viagem_user: user.Id, ...form}),
        });

        if (res.ok){
            alert("Perfil cadastrado com sucesso!");
            router.push('/lazeres')
        } else {
            alert("Erro ao cadastrar!");
        }
    };

    console.log(user?.Id)


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
                Olá, {user?.Nome}!
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

                {/*Card clima*/}
                <div style={cardStyle}>
                    <label style={labelStyle}>Qual o clima ideal<br></br> para você?</label>
                    <select
                        name="clima"
                        value={form.clima}
                        onChange={handleChange}
                        style={inputStyle}
                    >
                        <option value="Quente">Quente</option>
                        <option value="Tropical">Tropical</option>
                        <option value="Temperado">Temperado</option>
                        <option value="Frio">Frio</option>
                    </select>
                </div>
            
                {/*Card orçamento*/}
                <div style={cardStyle}>
                    <label style={labelStyle}>Qual seu orçamento para a viagem?</label>
                    <select
                        name="preco"
                        value={form.preco}
                        onChange={handleChange}
                        style={inputStyle}
                    >
                        <option value="Econômico">Econômico</option>
                        <option value="Médio">Médio</option>
                        <option value="Alto">Alto</option>
                        <option value="Luxo">Luxo</option>
                    </select>
                </div>

                {/*Card pessoas*/}
                <div style={cardStyle}>
                    <label style={labelStyle}>Qual será sua companhia de viagem?</label>
                    <select
                        name="companhia"
                        value={form.companhia}
                        onChange={handleChange}
                        style={inputStyle}
                    >
                        <option value="Sozinho">Sozinho</option>
                        <option value="Casal">Casal</option>
                        <option value="Família">Família</option>
                        <option value="Amigos">Amigos</option>
                    </select>
                </div>

                {/*Botão avançar*/}
                <button
                    type="submit"
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
            </form>
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

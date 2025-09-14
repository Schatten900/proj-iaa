"use client"
import { useState } from "react";
import { useRouter } from 'next/navigation'

export default function Cadastro() {
  const [form, setForm] = useState({
    nome: "",
    email: "",
    senha: "",
  });
  const router = useRouter()

  const [hover, setHover] = useState(false);


  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value});
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const res = await fetch("http://localhost:5000/api/user/cadastrar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });

    if (res.ok){
      alert("Usuário cadastrado com sucesso!");
      router.push('/login')
    } else {
      alert("Erro ao cadastrar!");
    }
  };


  return (
    <div style={{ display: "flex", height: "100vh"}}>
      {/* Lado da imagem */}
      <div style={{ flex: 1 }}>
        <img
          src="/aurora.jpg"
          alt="Cadastro"
          style={{ width: "100%", height: "100%", objectFit: "cover" }}
        />
      </div>

      {/* Lado da imagem */}
      <div
        style={{
          flex: 1,
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          background: "#F7F5F5",
        }}
        >
          <h1 style={{ fontSize: "3rem", fontWeight: "bold", marginBottom: "3rem", textShadow: "2px 2px 4px rgba(0,0,0,0.4)" }}>
            Cadastro
          </h1>
          <form
            onSubmit={handleSubmit}
            style={{ display: "flex", flexDirection: "column", width: "300px" }}
          >
            <label style={{ marginBottom: "0.5rem" }}>Nome</label>
            <input 
              name="nome"
              onChange={handleChange}
              style={{
                marginBottom: "1rem", // espaçamento entre os campos
                padding: "10px",
                background: "#E6E6E6",
                borderRadius: "15px",
                border: "none"
              }}
              />

            <label>E-mail</label>
            <input 
              name="email"
              onChange={handleChange}
              style={{
                marginBottom: "1rem", // espaçamento entre os campos
                padding: "10px",
                background: "#E6E6E6",
                borderRadius: "15px",
                border: "none"
              }}
              />

            <label>Senha</label>
            <input 
              name="senha"
              onChange={handleChange}
              style={{
                marginBottom: "1rem", // espaçamento entre os campos
                padding: "10px",
                background: "#E6E6E6",
                borderRadius: "15px",
                border: "none"
              }}
              />

            <button
              type="submit"
              onMouseEnter={() => setHover(true)}
              onMouseLeave={() => setHover(false)}
              style={{
                marginTop: "1rem",
                background: hover ? "#2E8B57": "#45736A", // muda a cor ao passar o mouse
                color: "#fff",
                padding: "10px",
                borderRadius: "20px",
                border: "none",
                cursor: "pointer",
                fontWeight: "bold",
                boxShadow: hover ? "0px 4px 12px rgba(0,0,0,0.3)" : "none", // sombra no hover
                transition: "all 0.3s ease", // animação suave
              }}>
                Cadastre-se
            </button>
          </form>
      </div>
    </div>


  );


}
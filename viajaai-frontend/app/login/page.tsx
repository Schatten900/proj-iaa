"use client"
import { useState } from "react";

export default function Login() {
  const [form, setForm] = useState({
    usuario: "",
    senha: "",
  });

  const [hover, setHover] = useState(false);


  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value});
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const res = await fetch("http://localhost:3001/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });

    if (res.ok){
      alert("Usuário autorizado com sucesso!");
    } else {
      alert("Erro ao autorizar!");
    }
  };


  return (
    <div style={{ display: "flex", height: "100vh"}}>
      {/* Lado da imagem */}
      <div style={{ flex: 1 }}>
        <img
          src="/aurora.jpg"
          alt="Login"
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
            Login
          </h1>
          <form
            onSubmit={handleSubmit}
            style={{ display: "flex", flexDirection: "column", width: "300px" }}
          >

            <label>Nome de usuário</label>
            <input 
              name="usuario"
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
              name="password"
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
                Entrar
            </button>

              <br></br>
            <h1 style={{ fontSize: "1rem", fontWeight: "medium", marginBottom: "3rem" }}>
            Não possui uma conta? Cadastre-se <a href="/cadastro" style={{color: "#45736A", textDecoration: "underline"}}>aqui</a>
            </h1>

          </form>
      </div>
    </div>


  );


}
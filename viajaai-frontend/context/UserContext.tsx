"use client";

import { createContext, useContext, useState, ReactNode, useEffect } from "react";

type User = {
    Id: number;
    Email: string;
    Nome: string;
    Senha: string;
};

type UserContextType = {
    user: User | null;
    setUser: (user: User | null) => void;
    logout: () => void;
};

const UserContext = createContext<UserContextType>({
    user: null,
    setUser: () => {},
    logout: () => {},
});

export const UserProvider = ({ children }: { children: ReactNode }) => {
    const [user, setUserState] = useState<User | null>(null);

    // Carrega usuário do localStorage ao iniciar
    useEffect(() => {
        const storedUser = localStorage.getItem("user");
        if (storedUser) setUserState(JSON.parse(storedUser));
    }, []);

    const setUser = (u: User | null) => {
        setUserState(u);
        if (u) localStorage.setItem("user", JSON.stringify(u));
        else localStorage.removeItem("user");
    };

    const logout = () => {
        setUser(null);
    };

    return (
        <UserContext.Provider value={{ user, setUser, logout }}>
            {children}
        </UserContext.Provider>
    );
};

export const useUser = () => useContext(UserContext);

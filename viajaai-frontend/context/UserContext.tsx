"use client";

import { createContext, useContext, useState, ReactNode } from "react";

type User = {
    Id: number;
    Email: string;
    Nome: string;
    Senha: string;
};

type UserContextType = {
    user: User | null;
    setUser: (user: User) => void;
};

const UserContext = createContext<UserContextType>({
    user: null,
    setUser: () => {},
});

export const UserProvider = ({ children }: { children: ReactNode }) => {
    const [user, setUser] = useState<User | null>(null);
    return (
        <UserContext.Provider value={{ user, setUser }}>
            {children}
        </UserContext.Provider>
    );
};

export const useUser = () => useContext(UserContext);
import React from "react";
import "./style.css";

export const Header: React.FC = () => {
    return (
        <header className="header">
            <h2 className="logo"><a href="/">Task Management</a></h2>

            <nav className="nav">
                <ul className="nav-list">
                    <li><a href="/login">ログイン</a></li>
                    <li><a href="/logout">ログアウト</a></li>
                </ul>
                <button>メニュー</button>
            </nav>
        </header>
    );
};
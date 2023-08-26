import React from "react";
import "../App.css";
import logo from "../assets/WhatsApp Image 2023-08-26 at 5.51.34 AM.jpeg"
import { Link } from 'react-router-dom'
export default function Navbar() {
  return (
    <>
    <div className="md:flex md:items-center md:justify-between m-4">
      <div className="min-w-0 flex-1">
      <img className="w-24 h-24 inline bg-transparent rounded-lg" src={logo} alt="logo" />
        <h2 className=" inline text-2xl font-bold leading-7 text-white sm:truncate sm:text-3xl sm:tracking-tight">
          Bandhu
        </h2>
      </div>
      <div className="mt-4 flex md:ml-4 md:mt-0">
        <Link to='/signup'>
        <button
          type="button"
          className="ml-3 inline-flex items-center rounded-md bg-blue-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-blue-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
        >
          Signup
        </button>
        </Link>
        <Link to='/login'>
        <button
          type="button"
          className="ml-3 inline-flex items-center rounded-md bg-blue-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-blue-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
        >
          Login
        </button>
        </Link>

      </div>
    </div>

    </>
  );
}

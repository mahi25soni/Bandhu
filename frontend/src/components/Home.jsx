import React, {useState, useEffect} from 'react'
import axios from 'axios'
import {useNavigate} from "react-router-dom";
const base_url = "http://127.0.0.1:8000/question/"
export default function Home() {
    const history = useNavigate()
    const [answer, setAnswer] = useState("")

    const your_question = (e) => {
        e.preventDefault();
        const temp_object = {
            question: e.target.elements["question"].value,
          };
          axios.post(base_url, temp_object).then((response) => {
            setAnswer(response.data)
          });
    }


  return (
    <>
    <div className='flex flex-col justify-center items-center align-middle'>

    <form onSubmit={your_question} className='flex-1  w-1/2 p-4 mt-20'>
        <input type="text" id="question" name='question'  className='w-4/5 h-9 rounded-md outline-none px-3 py-6'/>
        <button type='submit'  className='bg-slate-400 rounded-md text-white h-9 px-3 ml-4 hover:bg-black'>Send Message</button>
    </form>
    <div className='w-1/3 flex  p-2 text-xl font-bold text-white'>
        {answer}
    </div>
    </div>
    </>
  )
}

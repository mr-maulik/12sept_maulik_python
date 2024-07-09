import { useState } from 'react';
import Card from './components/Card';

function App() {
  const [count, setCount] = useState(0)
  let myObj ={
    username:"Shivam",
    age:27
  }
  let newArr=[1,2,3]

  return (
    <>
      <h1 className='bg-green-400 text-black p-4 rounded-xl mb-4 text-center w-80 mx-auto'>tailwind Test</h1>
      <Card username="Tailwind" btnText="click me" />
      <Card username="Props"/>
    </>
  )
}

export default App

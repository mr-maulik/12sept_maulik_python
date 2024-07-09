import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { increment, decrement, reset } from './features/counterSlice';

function Counter() {
  const count = useSelector((state) => state.counter.value);
  const dispatch = useDispatch();

  return (
    <div className="bg-light text-center pt-5" style={{ height : "100vh" }}>
      <div className="mb-4">Counter: {count}</div>
      <div className="">
        <button
          onClick={() => dispatch(increment())}
          className="px-4 py-2 bg-black mx-3  text-white"
        >
          Increment
        </button>
        <button
          onClick={() => dispatch(decrement())}
          className="px-4 py-2 bg-black mx-3 text-white"
        >
          Decrement
        </button>
      </div>
    </div>
  );
}

export default Counter;

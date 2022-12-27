import React from 'react'
import "./Count.css"

export default function Count({data,label}) {
  return (
    <div className='count_container'>
    
    <h3> {label} </h3>


    <h1>{data}</h1>
   
    
    
    </div>
  )
}


import './App.css';
import {DemoArea} from '../src/components/GroupedBar'
import TopBar from './components/TopBar';
import Count from './components/Count';
import axios from 'axios';
import {useState,useEffect} from 'react'


function App() {

  const [accept, setAcceptData] = useState([])
  const [denied, setDenyData] = useState([])

  const [single_deny, setSingleDeny] = useState()
  const [single_accept, setSingleAccept] = useState()
  


  const getAcceptData = async () => {
      const data = await axios.get('http://localhost:888/accept')


      setAcceptData(data.data)
      console.log(accept)



  }


  const getDenyData = async () => {
    const data = await axios.get('http://localhost:888/denied')
    // console.log(data.data)

    setDenyData(data.data)
    console.log(denied)


}

const getSingleDeny = async () => {
  const data = await axios.get('http://localhost:888/single_denied')
  // console.log(data.data)

  setSingleDeny(data.data)
  console.log(single_deny)


}

const getSingleAccept = async () => {
  const data = await axios.get('http://localhost:888/single_accept')
  // console.log(data.data)

  setSingleAccept(data.data)
  console.log(single_accept)


}



  useEffect(() => {

    getAcceptData()
    getDenyData()
    getSingleAccept()
    getSingleDeny()

  },[])


  return (

    <>
   {/* <TopBar /> */}
<div className='container'> 
    
  <div className='graph'> 

  <DemoArea data={accept} label={"ACCEPT"}/>
    <Count data={single_accept} label={"ACCEPT"} />
  

  </div>


  <div className='graph'>
  <DemoArea data={denied} label={"REJECT"}/>
    <Count data={single_deny} label={"REJECT"}/>

  </div>


     </div>

     

     {/* <TopBar /> */}
    </>

  );
}

export default App;

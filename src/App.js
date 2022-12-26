
import './App.css';
import {DemoArea} from '../src/components/GroupedBar'
import TopBar from './components/TopBar';
import Count from './components/Count';
import axios from 'axios';
import {useState,useEffect} from 'react'


function App() {

  const [accept, setAcceptData] = useState([])
  const [denied, setDenyData] = useState([])
  


  const getAcceptData = async () => {
      const data = await axios.get('http://localhost:888/accept')


      setGraphData(data.data)


  }


  const getDenyData = async () => {
    const data = await axios.get('http://localhost:888/denied')
    // console.log(data.data)

    setGraphData(data.data)


}



  useEffect(() => {

    getAcceptData()
    getDenyData()

  },[])


  return (

    <>
   <TopBar />
<div className='container'> 
    
 
    <DemoArea data={accept}/>
    <Count data />
    <DemoArea data={denied}/>
    <Count data />

    
     </div>

     

     {/* <TopBar /> */}
    </>

  );
}

export default App;

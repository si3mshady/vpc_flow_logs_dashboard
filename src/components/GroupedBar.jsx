import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import { Column } from '@ant-design/plots';

export const DemoArea = ({data, label}) => {
//   const [data, setData] = useState([]);


  

  const config = {
    data,
    color: label == 'ACCEPT' ? 'green' : 'red',
    xField: 'interface_id',
    yField: 'count',
    xAxis: {
      range: [0, 1],
    //   tickCount: 5,
    },
    areaStyle: () => {
      return {
        fill: 'l(270) 0:#c32aff 0.5:#c32aff 1:#c32aff',
      };
    },
  };

  return <Column  style={{backgroundColor:'black'}} {...config} />;
};


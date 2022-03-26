import logo from './logo.svg';
import './App.css';
import axios from 'axios';

import { useEffect } from 'react';
import { Upload, message, Button } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import 'antd/dist/antd.css';

function App() {

  const props = {
    name: 'file',
    accept: '.pdf,.doc,.docx',
    action: 'http://127.0.0.1:5000/api/v0/',
    headers: {
      authorization: 'authorization-text',
    },
    maxCount: 1,
    onChange(info) {
      if (info.file.status !== 'uploading') {
        console.log(info.file, info.fileList);
      }
      if (info.file.status === 'done') {
        message.success(`${info.file.name} file uploaded successfully`);
      } else if (info.file.status === 'error') {
        message.error(`${info.file.name} file upload failed.`);
      }
    },
  };

  useEffect(() => {
    console.log("hello");
    const query = "machine learning engineer"
    axios.post('http://127.0.0.1:5000/api/v0/pull', {"search_query": query})
      .then(res => console.log(res))
      .catch(err => console.log(err))
  }, [])
  
  return (
    <Router>
      <Switch>
        <Route exact path='/'>
          <div className="App">
            <header className="App-header">
              <div>
                Resume Oracle: Find Your Dream Job!
              </div>
              <Upload {...props}>
                <Button size={"large"} icon={<UploadOutlined />}>Click to Upload</Button>
              </Upload>
            </header>
          </div>
        </Route>
        <Route exact path='/search'>
          <SearchResults />
        </Route>
      </Switch>
    </Router>
    
  );
}

export default App;

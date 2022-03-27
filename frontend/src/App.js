import './App.css';

import { useState } from 'react';
import { Upload, message, Button, Layout, PageHeader, Card } from 'antd';
import { UploadOutlined, StepBackwardOutlined } from '@ant-design/icons';
import { CompanyCard } from './CompanyCard';
import 'antd/dist/antd.css';

const { Header, Footer, Sider, Content } = Layout;

function App() {
  const [data, setData] = useState([])
  const props = {
    name: 'file',
    accept: '.pdf,.doc,.docx',
    action: 'https://resumeoraclebackend.herokuapp.com/api/v0/',
    headers: {
      authorization: 'authorization-text',
    },
    maxCount: 1,
    onChange(info) {
      if (info.file.status !== 'uploading') {
        console.log(info.file, info.fileList);
      }
      if (info.file.status === 'done') {
        setData(() => info.file.response.payload);
        message.success(`${info.file.name} file uploaded successfully`);
      } else if (info.file.status === 'error') {
        message.error(`${info.file.name} file upload failed.`);
      }
    },
  };

  return (

    <div className="App">
      <header className="App-header">
        {data.length > 0 ? (
          <div>
            <Layout className="layout" style={{width: '100vw', height: '100vh'}}>
              <Content style={{ padding: '0 50px', overflowY: 'scroll' }}>
                <PageHeader onBack={() => setData([])} title="Return" subTitle="upload another resume?" />
                <Card title="Relevant Jobs">
                  {data.map((company) => {
                    return <Card.Grid style={{width:"50%"}}><CompanyCard company={company}/></Card.Grid>
                  })}
                </Card>
                {/* {data.map((company) => {
                  return <CompanyCard company={company}/>
                })} */}
              </Content>
              <Footer style={{textAlign: 'center', background: '#282c34', color: 'white'}}>ResumeOracle © 2022</Footer>
            </Layout>
            
            
          </div>
        ): (
          <div>
            <div>Resume Oracle: Find Your Dream Job!</div>
            <Upload {...props}>
              <Button size={"large"} icon={<UploadOutlined />}>Click to Upload</Button>
            </Upload>
          </div>
        )}
        
      </header>
    </div>
    
  );
}

export default App;

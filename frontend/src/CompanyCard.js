import { Button, Divider } from 'antd';
import { RightCircleOutlined } from '@ant-design/icons';
export const CompanyCard = ({company}) => {
    return (
        <div style={{display: 'flex', flexDirection: 'row', height: 150}}>
            <div style={{width: '80%'}}>
                <div><b>{company.company}</b> - {company.title}</div>
                <Divider />
                <p>{company.description.substring(0, 200)+'...'}</p>
            </div>
            <div style={{width: '20%', display: 'flex', alignItems:'center', justifyContent:'center'}}></div>
            <a href={company.link} target="_blank"><Button><RightCircleOutlined /></Button></a>
        </div>
    );
}
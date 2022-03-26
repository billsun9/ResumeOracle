import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

export const SearchResults = (props) => {
    const params = useParams()
    const [data, setData] = useState({});
    useEffect(() => {
        var config = {
            method: 'get',
            url: `${BASE_URL}/creator_info/${params.id}`,
            headers: { 
                'Content-Type': 'text/plain'
            }
        };

        axios(config)
            .then(function (response) {
                console.log(response.data)
                setData(() => response.data);
                if(Object.keys(data).length !== 0) console.log(data);
            })
            .catch(function (error) {
            console.log(error);
            });
    }, [])

    return (
        <div style={{minHeight: '100vh',
        display: 'flex',
        alignItems:'center',
        justifyContent:'center',
        background:'#FFFF8A'
    }}>
        <div style={{display: 'flex',
        minWidth: '60%',
        minHeight: '80%',
        flexDirection: 'column',
        alignItems:'center',
        justifyContent:'center',
        background: '#f4ffb8',
        padding: '12px 22px',
        borderRadius: '18px'}}>
            {Object.keys(data).length !== 0 && (
                <div> 
                    <h2>Content Creator: {data['name']}</h2>
                    {/* <Carousel style={{width: '50vw', height: '20vh'}} autoplay>
                        <div style={{height: 180, width: 180, textAlign: 'center'}}>Hey!</div>
                        <div style={{height: 180, width: 180, textAlign: 'center'}}>Bye!</div>
                    </Carousel> */}
                    <div style={{padding: 30, background: '#ececec'}}>
                        {data.channel.scraped.views > 0 && (
                            <Card title="YouTube Channel" bordered={false} style={{ width: 300 }}>
                                <p>Subscribers: {data.channel.scraped.subscribers}</p>
                                <p>Cumulative Views: {data.channel.scraped.views}</p>
                            </Card>
                        )}
                        
                        {data.tiktok.scraped.views !== 0 && (
                            <Card title="TikTok Channel" bordered={false} style={{ width: 300 }}>
                                <p>Subscribers: {data.tiktok.scraped.subscribers}</p>
                                <p>Cumulative Views: {data.tiktok.scraped.views}</p>
                            </Card>
                        )}
                        {data.tiktok.scraped.views !== 0 && (
                            <Card title="TikTok Channel" bordered={false} style={{ width: 300 }}>
                                <p>Subscribers: {data.tiktok.scraped.subscribers}</p>
                                <p>Cumulative Views: {data.tiktok.scraped.views}</p>
                            </Card>
                        )}
                        <div style={{display: 'block'}}>
                            Specialities: {data.specialtyAreas}
                        </div>
                    </div>
                </div>
            )}
            

        </div>
    </div>
    );
}
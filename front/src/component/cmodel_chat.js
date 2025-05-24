import React from 'react';
import { Ccard } from './Ccard.js';
import { Input } from '@lobehub/ui';
import { Button } from '@lobehub/ui';
import * as BookOpenCheck from 'lucide-react';
import { Spin } from '@arco-design/web-react';


export const FrostedWindow = ({ set_show_chat }) => {
    const [input_value, set_input_value] = React.useState("");
    const [card_list, set_card_list] = React.useState([]);
    // const containerStyle = {

    //     height: '90vh',
    //     position: 'position',
    //     top: '1vh',
    //     left: '30px',
    //     right: '30px',
    //     // bottom: '30px',
    //     borderRadius: '12px',
    //     backgroundColor: 'rgba(255, 255, 255, 0.5)',
    //     backdropFilter: 'blur(10px)',
    //     WebkitBackdropFilter: 'blur(10px)', // 兼容Safari
    //     boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.37)',
    //     border: '1px solid rgba(255, 255, 255, 0.18)',
    //     overflow: 'hidden',
    //     zIndex: 9999,
    // };

    // const contentStyle = {
    //     padding: '20px',
    //     height: '100%',
    //     overflow: 'auto',
    //     position: 'position',
    // };
    // const closeButtonStyle = {
    //     position: 'position',
    //     right: '20px',
    //     top: '20px',
    //     width: '32px',
    //     height: '32px',
    //     borderRadius: '50%',
    //     background: 'rgba(255, 255, 255, 0.8)',
    //     border: 'none',
    //     cursor: 'pointer',
    //     display: 'flex',
    //     alignItems: 'center',
    //     justifyContent: 'center',
    //     boxShadow: '0 2px 6px rgba(0, 0, 0, 0.1)',
    //     transition: 'all 0.2s ease',
    //     ':hover': {
    //         background: 'rgba(255, 255, 255, 1)',
    //         transform: 'scale(1.1)'
    //     }
    // };
    const containerStyle = {

        height: '90vh',
        position: 'fixed',
        top: '-100px',
        left: '30px',
        right: '30px',
        bottom: '150px',
        borderRadius: '12px',
        backgroundColor: 'rgba(255, 255, 255, 0.5)',
        backdropFilter: 'blur(10px)',
        WebkitBackdropFilter: 'blur(10px)', // 兼容Safari
        boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.37)',
        border: '1px solid rgba(255, 255, 255, 0.18)',
        overflow: 'hidden',
        zIndex: 9999,
    };

    const contentStyle = {
        padding: '20px',
        height: '100%',
        overflow: 'auto',
    };
    const closeButtonStyle = {
        position: 'absolute',
        right: '20px',
        top: '20px',
        width: '32px',
        height: '32px',
        borderRadius: '50%',
        background: 'rgba(255, 255, 255, 0.8)',
        border: 'none',
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        boxShadow: '0 2px 6px rgba(0, 0, 0, 0.1)',
        transition: 'all 0.2s ease',
        ':hover': {
            background: 'rgba(255, 255, 255, 1)',
            transform: 'scale(1.1)'
        }
    };
    return (
        <div style={containerStyle}>
            <div style={contentStyle}>
                <div className='content' style={{ width: '100%', height: '88%', overflow: 'auto', }}>
                    <h1 style={{ margin: "0px", color: '#4368ff', textAlign: 'center' }}>账号助手</h1>
                    {/* <Ccard imageUrl={"https://pzdsoss.pzds.com/c/2/goods/cover/20250506/tools_U2bmdNrL_1746531513966.jpg?x-oss-process=style/titleImg"
                    } title={"账号助手"} subtitle={"账号助手"} />
                    <Ccard imageUrl={"https://pzdsoss.pzds.com/c/2/goods/cover/20250506/tools_U2bmdNrL_1746531513966.jpg?x-oss-process=style/titleImg"
                    } title={"账号助手"} subtitle={"账号助手"} />
                    <Ccard imageUrl={"https://pzdsoss.pzds.com/c/2/goods/cover/20250506/tools_U2bmdNrL_1746531513966.jpg?x-oss-process=style/titleImg"
                    } title={"账号助手"} subtitle={"账号助手"} />
                    <Ccard imageUrl={"https://pzdsoss.pzds.com/c/2/goods/cover/20250506/tools_U2bmdNrL_1746531513966.jpg?x-oss-process=style/titleImg"
                    } title={"账号助手"} subtitle={"账号助手"} in_search={false} helf='https://www.pzds.com/goodsDetails/TD2W2X/6' />
                    <Ccard imageUrl={"https://pzdsoss.pzds.com/c/2/goods/cover/20250506/tools_U2bmdNrL_1746531513966.jpg?x-oss-process=style/titleImg"
                    } title={"账号助手"} subtitle={"账号助手"} />
                    <Ccard imageUrl={"https://pzdsoss.pzds.com/c/2/goods/cover/20250506/tools_U2bmdNrL_1746531513966.jpg?x-oss-process=style/titleImg"
                    } title={"账号助手"} subtitle={"账号助手"} />
                    <Ccard imageUrl={"https://pzdsoss.pzds.com/c/2/goods/cover/20250506/tools_U2bmdNrL_1746531513966.jpg?x-oss-process=style/titleImg"
                    } title={"账号助手"} subtitle={"账号助手"} />
                    <Ccard imageUrl={"https://pzdsoss.pzds.com/c/2/goods/cover/20250506/tools_U2bmdNrL_1746531513966.jpg?x-oss-process=style/titleImg"
                    } title={"账号助手"} subtitle={"账号助手"} />
                    <Ccard imageUrl={"https://pzdsoss.pzds.com/c/2/goods/cover/20250506/tools_U2bmdNrL_1746531513966.jpg?x-oss-process=style/titleImg"
                    } title={"账号助手"} subtitle={"账号助手"} /> */}
                    {card_list}
                </div>
                <Spin dot={true} />
                <div className='input_box' style={{ width: '100%', height: '10%' }}>
                    <div style={{
                        display: 'flex',
                        alignItems: 'center',       // 垂直居中
                        //   justifyContent: 'space-between', // 可选：自动分配间距
                        width: '100%',             // 控制整体宽度
                        gap: '10px',            // 控制两个组件之间的空隙   
                        justifyContent: "center", // 水平居中
                    }}>
                        <Input
                            type="text"
                            placeholder="简单描述一下你想要你的账号"
                            shadow={true}
                            variant="filled"
                            style={{
                                color: '#4368ff',
                                width: '80%',
                            }}
                            value={input_value}
                            onChange={(e) => {
                                set_input_value(e.target.value);
                            }}
                        />
                        <Button
                            glass={true}
                            // size="default"
                            // type='primary'
                            // color="default" 
                            variant="solid"
                            icon={BookOpenCheck.BookOpenCheck}
                            style={{

                            }}
                            onClick={() => {
                                if (input_value === "") {
                                    alert("请输入内容");
                                    return;
                                }
                                // 发送请求

                                set_input_value("");
                                set_card_list([]);

                                fetch(`http://localhost:8000/chat?query=${input_value}`, {
                                    method: 'get',
                                    headers: {
                                        'Content-Type': 'application/json',
                                    }
                                }).then(response => response.json())
                                    .then(data => {
                                        console.log("=------------------------------------")
                                        const parsedData = typeof data === 'string' ? JSON.parse(data) : data;
                                        console.log(parsedData)
                                        set_card_list(parsedData["data"]["records"].map((item, index) => {
                                            return <Ccard imageUrl={item.goodsImg}
                                                title={item.title} subtitle={item.simpleMessage} current_state={"已完成"} helf={"https://www.pzds.com/goodsDetails/" + item.goodsNo + "/6" } price={item.price}/>
                                        }
                                        ));
                                    });
                            }}
                        > 查询
                        </Button>

                    </div>

                </div>
                <button
                    style={closeButtonStyle}
                    onClick={() => set_show_chat(false)}
                    aria-label="Close"
                >
                    <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                        <path d="M13 1L1 13M1 1L13 13" stroke="#666" strokeWidth="2"
                            strokeLinecap="round" strokeLinejoin="round" />
                    </svg>
                </button>
            </div>
        </div>
    );
};

// export default FrostedWindow;
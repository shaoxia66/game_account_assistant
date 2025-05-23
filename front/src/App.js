import './App.css';
import { AuroraBackground ,GradientButton} from '@lobehub/ui/awesome';
import { ThemeProvider } from '@lobehub/ui'
import { useRef, useEffect,useState } from 'react';
import bgImage from './assets/img/bg-20250430.webp';
import { FrostedWindow } from './component/cmodel_chat.js';
function App() {
  const [show_chat,set_show_chat] = useState(false);
  const move_Ref = useRef(null);
  useEffect(() => {
    if (move_Ref.current) {
      setTimeout(() => {
        move_Ref.current.classList.add('loaded');
      }, 1000); // 延迟1秒后添加类名
      
    }
  }, []);

  return (
    <div className="App">
      <ThemeProvider appearance={'dark'} enableGlobalStyle={true}>
        <div className='background' style={{
          position: 'fixed', /* 或 absolute（根据需求） */
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          zIndex: -2, /* 关键：置于最底层 */
          pointerEvents: 'none' /* 防止遮挡页面交互 */
        }} >
          <AuroraBackground />

        </div>
        <div className='background' style={{
          position: 'fixed', /* 或 absolute（根据需求） */
          top: 0,
          left: -200,
          width: '100%',
          height: '100%',
          zIndex: -1, /* 关键：置于最底层 */
          pointerEvents: 'none', /* 防止遮挡页面交互 */
          WebkitMaskImage: "linear-gradient(to right, black 0%, transparent 50%)",
          maskImage: "linear-gradient(to right, black 0%, transparent 50%)",
          // 可选：添加背景样式用于观察效果
          backgroundColor: "blue" // 示例颜色
        }} >
          <img style={{
            width: "100%",
            height: "100%",
            objectFit: "fill" // 确保拉伸填充（允许变形）
          }} src={bgImage} alt="背景图片" />

        </div>
        <div className="move"  ref={move_Ref} 
          style={{
          fontFamily: "Smiley Sans Oblique",
          background: "linear-gradient(to right,  #4368ff, #efceff)",
          WebkitBackgroundClip: "text",
          color: "transparent",
        }}>
          <div style={{ fontSize: "80px", color: "rgba(255, 255, 255, 0.9)" }}>游 戏 账 号</div>
          <div style={{ fontSize: "110px" ,background: "linear-gradient(to right,  #4368ff, #efceff)",
          WebkitBackgroundClip: "text",color: "transparent", }} >推 荐 助 手</div>
          <div>
          <GradientButton onClick={() => {
            set_show_chat(true);
          }} style={{
            
            marginTop: "15px",
            fontFamily: "Smiley Sans Oblique",
            fontSize: "30px",      // 放大文字
            padding: '30px 50px', // 调整内边距（上下 8px，左右 16px）
          }} >开 始 使 用</GradientButton>
          </div>
          {show_chat && <FrostedWindow set_show_chat={set_show_chat}/>}
        </div>
      </ThemeProvider>

    </div>
  );
}

export default App;

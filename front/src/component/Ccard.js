import React, { useState, useEffect } from 'react';
import styles from './Card.module.css'; // 假设你使用 CSS Modules

export const Ccard = ({ imageUrl, title, subtitle,current_state="评估中",helf="",price}) => {
  const [isHovered, setIsHovered] = useState(false);
  const [isVisible, setIsVisible] = useState(false); // 用于进入动画
  useEffect(() => {
    // 模拟组件挂载后触发进入动画
    const timer = setTimeout(() => {
      setIsVisible(true);
    }, 100); // 稍微延迟一下，确保组件渲染

    return () => clearTimeout(timer);
  }, []);

  const handleMouseEnter = () => {
    setIsHovered(true);
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  return (
    <div
      className={`${styles.card} ${isVisible ? styles.appear : ''}  ${current_state==="评估中" ? styles.rotating : ''}`} // 应用进入动画类
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      <div className={styles.cardImageContainer} onClick={() => { 
        if (helf!==''){
            window.open(helf, '_blank');
        }
      }}>
        <img
          src={imageUrl}
          alt="Card Visual"
          className={styles.cardImage}
          // 可以根据 isHovered 状态添加额外的样式或动画类
          // style={{ transform: isHovered ? 'scale(1.05)' : 'scale(1)' }}
        />
      </div>
      <div className={styles.cardContent}>
        <p className={styles.cardTitle}>{"价格："+price}</p>
        {/* <div className={styles.cardState}>{current_state}</div> */}
        {/* <h3 className={styles.cardTitle}>{title}</h3> */}
        {/* <p className={styles.cardSubtitle}>{subtitle}</p> */}
        <p className={styles.cardTitle}>{title}</p>
        <p className={styles.cardSubtitle}>{subtitle}</p>
      </div>
    </div>
  );
};

export default Ccard;
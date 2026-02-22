import React, { useState, useEffect } from 'react';
import { createRoot } from 'react-dom/client';

const HelloWorldView = ({ data, onAction, onRefresh }) => {
  const [localCounter, setLocalCounter] = useState(data?.counter || 0);

  const handleButtonClick = async () => {
    // 调用后端注册的 action="update_counter"
    const result = await onAction('update_counter', {});
    if (result && result.ok) {
      setLocalCounter(result.new_counter);
      onRefresh(); // 刷新全局数据
    }
  };

  return (
    <div style={{ padding: '20px', backgroundColor: '#f0f9ff', borderRadius: '8px', border: '1px solid #bae6fd' }}>
      <h2 style={{ color: '#0369a1', marginBottom: '10px' }}>🌍 Hello World Plugin</h2>
      <p style={{ fontSize: '16px', color: '#334155' }}>{data?.message || 'Loading...'}</p>
      
      <div style={{ marginTop: '20px', padding: '15px', background: 'white', borderRadius: '6px' }}>
        <p><strong>Local Counter:</strong> {localCounter}</p>
        <p><strong>Last Server Interaction:</strong> {data?.last_interaction}</p>
        
        <button 
          onClick={handleButtonClick}
          style={{
            marginTop: '10px',
            padding: '8px 16px',
            backgroundColor: '#0284c7',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          Click Me!
        </button>
      </div>
      
      <p style={{ marginTop: '15px', fontSize: '12px', color: '#64748b' }}>
        This view is dynamically loaded from your GitHub repository.
      </p>
    </div>
  );
};

// 导出适配器，使 OpenSquad 前端能够挂载此组件
let root: any = null;

export const mount = (el: HTMLElement, props: any) => {
  root = createRoot(el);
  root.render(<HelloWorldView {...props} />);
};

export const unmount = () => {
  if (root) {
    root.unmount();
    root = null;
  }
};

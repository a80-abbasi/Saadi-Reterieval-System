import React from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { store } from './app/store';
import App from './App';
import reportWebVitals from './reportWebVitals';
import './index.css';
import './assets/fonts/Lalezar-Regular.ttf';
import './assets/fonts/IranNastaliq.ttf';
import './assets/fonts/B-NAZANIN.ttf';


import './assets/fonts/IranNastaliq_1.ttf';
import './assets/fonts/Dima Shekasteh.ttf';
import './assets/fonts/Shekasteh V2.001.ttf';



const container = document.getElementById('root')!;
const root = createRoot(container);

root.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

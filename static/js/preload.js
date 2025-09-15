const { contextBridge, shell, ipcRenderer } = require('electron');
const path = require('path');
const { remote } = require('@electron/remote/main')

// 与 main.js 保持一致的服务器配置
const HOST = '127.0.0.1'
const PORT = 3456
// 获取从主进程传递的配置数据
const windowConfig = {
    windowName: "default",
};
// 暴露基本的ipcRenderer给骨架屏页面使用
contextBridge.exposeInMainWorld('electron', {
  isMac: process.platform === 'darwin',
  isWindows: process.platform === 'win32',
  ipcRenderer: {
    on: (channel, func) => {
      // 只允许特定的通道
      const validChannels = ['backend-ready'];
      if (validChannels.includes(channel)) {
        ipcRenderer.on(channel, (event, ...args) => func(...args));
      }
    }
  },
  // 暴露服务器配置
  server: {
    host: HOST,
    port: PORT
  },
  requestStopQQBot: () => ipcRenderer.invoke('request-stop-qqbot'),
});

// 暴露安全接口
contextBridge.exposeInMainWorld('electronAPI', {
  // 系统功能
  openExternal: (url) => shell.openExternal(url),
  openPath: (filePath) => shell.openPath(filePath),
  getAppPath: () => app.getAppPath(),
  getPath: () => remote.app.getPath('downloads'),
  // 窗口控制
  windowAction: (action) => ipcRenderer.invoke('window-action', action),
  onWindowState: (callback) => ipcRenderer.on('window-state', callback),

  // 文件对话框
  openFileDialog: () => ipcRenderer.invoke('open-file-dialog'),
  openImageDialog: () => ipcRenderer.invoke('open-image-dialog'),
  readFile: (filePath) => ipcRenderer.invoke('readFile', filePath),
  // 路径处理
  pathJoin: (...args) => path.join(...args),
  sendLanguage: (lang) => ipcRenderer.send('set-language', lang),
  // 环境检测
  isElectron: true,

  // 自动更新
  checkForUpdates: () => ipcRenderer.invoke('check-for-updates'),
  downloadUpdate: () => ipcRenderer.invoke('download-update'),
  quitAndInstall: () => ipcRenderer.invoke('quit-and-install'),
  onUpdateAvailable: (callback) => ipcRenderer.on('update-available', callback),
  onUpdateNotAvailable: (callback) => ipcRenderer.on('update-not-available', callback),
  onUpdateError: (callback) => ipcRenderer.on('update-error', callback),
  onDownloadProgress: (callback) => ipcRenderer.on('download-progress', callback),
  onUpdateDownloaded: (callback) => ipcRenderer.on('update-downloaded', callback),
  showContextMenu: (menuType, data) => ipcRenderer.invoke('show-context-menu', { menuType, data }),
  //保存环境变量
  setNetworkVisibility: (visible) => ipcRenderer.invoke('set-env', { key: 'networkVisible', value: visible }), 
  //重启app
  restartApp: () => ipcRenderer.invoke('restart-app'),
  startVRMWindow: (windowConfig) => ipcRenderer.invoke('start-vrm-window', windowConfig),
  stopVRMWindow: () => ipcRenderer.invoke('stop-vrm-window'),
  getServerInfo: () => ipcRenderer.invoke('get-server-info'),
  setIgnoreMouseEvents: (ignore, options) => ipcRenderer.invoke('set-ignore-mouse-events', ignore, options),
  getIgnoreMouseStatus: () => ipcRenderer.invoke('get-ignore-mouse-status'),
  downloadFile: (payload) => ipcRenderer.invoke('download-file', payload),
    // 修改：添加回调参数
    getWindowConfig: (callback) => {
        if (windowConfig.windowName !== "default") {
            // 如果配置已更新，直接返回
            callback(windowConfig);
        } else {
            // 如果配置未更新，监听更新事件
            const handler = (event) => {
                callback(event.detail);
                window.removeEventListener('window-config-updated', handler);
            };
            window.addEventListener('window-config-updated', handler);
        }
    },
});

// 在文件末尾添加以下代码来接收主进程传递的配置
ipcRenderer.on('set-window-config', (event, config) => {
    Object.assign(windowConfig, config);
    console.log('收到窗口配置:', windowConfig);
    
    // 添加：配置更新后发送事件通知页面
    window.dispatchEvent(new CustomEvent('window-config-updated', {
        detail: windowConfig
    }));
});

data = {
    "versionName": "0.26",
    "versionCode": 3,
    "history": {
        "0.20": "完全重写, 支持出征\n交流群:560271993",
        "0.21": "新增 错误处理, 可长时间挂机\n修改部分出错的表述\n分解里保留星级应该是分解星级\n更新请去群文件自取\n交流群:560271993",
        "0.22": "修复 无法迂回问题\n优化 任务将自动排序\n新增 错误日志功能, 方便上传日志\n更新请去群文件自取\n交流群:560271993",
        "0.23": "修复 无法过资源点问题\n新增 网络连接失败自动重试\n提高稳定性\n更新请去群文件自取\n交流群:560271993",
        "0.24": "新增 活动适配\n更新请去群文件自取\n交流群:560271993",
        "0.25": "修复 活动结束后无法进入游戏问题\n交流群:560271993",
        "0.26": "本次没有任何更新\n旧服务器即将停止服务\n新版下载地址 github上关注bcxmzbcxm 或560271993群内下载"
    },


}

import json
with open("data/version.json", 'w') as f:
    f.write(json.dumps(data))

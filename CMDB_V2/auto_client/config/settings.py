#!/usr/bin/env python3
# 当前引擎
ENGINE = "agent"

# SSH模式相关配置
SSH_PRIVATE_KEY = "/root/.ssh/sefs.key"
SSH_PORT = 22
SSH_USER = "root"

# 引擎插件列表
ENGINES_DICT = {
    "ssh": "src.engines.ssh.SSHHandle",
    "salt": "src.engines.salt.SaltHandle",
    "agent": "src.engines.agent.AgentHandle",
}

# 插件列表
PLUGINS_DICT = {
    "cpu": "src.plugins.cpu.CPU",
    "disk": "src.plugins.disk.Disk",
    "memory": "src.plugins.memory.Memory",
}



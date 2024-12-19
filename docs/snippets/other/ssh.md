# SSH

## Schlüsselpaar erstellen

```bash
ssh-keygen -t ed25519 -C "your_email@example.com" -f ~/.ssh/id_ed25519
```

## Konfigurationsdatei

<!-- --8<-- [start:ssh-config] -->
```bash title="~/.ssh/config"
Host 192.168.178.204
    User git
    Hostname 192.168.178.204
    Port 2222
    Preferredauthentications publickey
    IdentityFile ~/.ssh/id_ed25519
    TCPKeepAlive yes
    AddKeysToAgent yes
```
<!-- --8<-- [end:ssh-config] -->

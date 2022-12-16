# ViewBPF

ViewBPF, a frontend eBPF program results viewer.

## Building

There were four components need to setup.
The following steps can use on Arch-based Linux.

### Redis

```shell
$ sudo pacman -S redis
$ sudo systemctl enable redis.service --now
```

### Backend

```shell
$ python -m venv venv
$ pip install -R requirements.txt
$ python app.py
```

### Frontend

Currently, there is no static building frontend, so it uses vite.

```shell
$ npm install
$ npm run dev
```

### Runner

Since `bcc` needs privilege, so write it as another python app.

```shell
$ sudo pacman -S bcc
$ sudo python run.py
```

## Page

http://localhost:5173

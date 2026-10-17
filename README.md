# Uptime Monitor

A simple tool that checks if websites are up. It runs automatically every 5 minutes with cron and saves the results in a log file.

This is my first DevOps learning project. I'm building it step by step, adding a new tool at each stage.

## How it works

1. `sites.txt` contains a list of websites.
2. `check.sh` checks each website with `curl` and reads the HTTP status code.
3. Code `200` means the site is **UP**. Any other code means it's **DOWN**.
4. cron runs the script every 5 minutes and adds the results to `uptime.log`.

## Run with Docker

```bash
docker build -t uptime-monitor .
docker run uptime-monitor
```

## Example output

```
2026-10-12 18:20:15 UP    https://www.google.com
2026-10-12 18:20:15 UP    https://github.com
2026-10-12 18:20:16 DOWN  https://this-site-does-not-exist-12345.com (000)
```

## How to run it

```bash
git clone git@github.com:Bartlomiej991/uptime-monitor.git
cd uptime-monitor
chmod +x check.sh
./check.sh
```

To run it automatically every 5 minutes, add this line with `crontab -e`:

```
*/5 * * * * cd /path/to/uptime-monitor && ./check.sh >> uptime.log 2>&1
```
## Run with Docker

```bash
docker build --tag uptime-monitor .
docker run uptime-monitor
```

## Tools used

- Linux (Linux Mint)
- Bash
- curl
- cron
- Git and GitHub
- Docker

## Roadmap

- [x] Bash script that checks websites
- [x] Automatic checks with cron and a log file
- [x] Version control with Git and GitHub
- [x] Docker container
- [ ] Web page with the results (Python, Flask)
- [ ] CI/CD with GitHub Actions
- [ ] Deploy to AWS with Terraform
- [ ] Monitoring with Prometheus and Grafana

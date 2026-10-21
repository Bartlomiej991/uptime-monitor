# Uptime Monitor

A simple tool that checks if websites are up.

This is my first DevOps learning project. I'm building it step by step, adding a new tool at each stage.

## How it works

1. `sites.txt` contains a list of websites.
2. `check.py` sends a request to each website and reads the HTTP status code.
3. Code `200` means the site is **UP**. Any other code means it's **DOWN**.
4. If a website doesn't answer at all (DNS error, timeout), the script marks it as **DOWN (no answer)** and continues with the next site.

The first version of the project was written in Bash (`check.sh`) with `curl`. It's still in the repository.

## Example output

```
2026-10-20 20:07:38 UP https://www.google.com
2026-10-20 20:07:38 UP https://github.com
2026-10-20 20:07:38 DOWN https://this-site-does-not-exist-12345.com no answer
2026-10-20 20:07:38 DOWN https://httpbin.org/status/404 404
Checked 4 sites
```

## How to run it (Python version)

```bash
git clone git@github.com:Bartlomiej991/uptime-monitor.git
cd uptime-monitor
sudo apt install -y python3-requests
python3 check.py
```

## Bash version and cron

```bash
chmod +x check.sh
./check.sh
```

To run it automatically every 5 minutes, add this line with `crontab -e`:

```
*/5 * * * * cd /path/to/uptime-monitor && ./check.sh >> uptime.log 2>&1
```

## Run with Docker

The Docker image currently runs the Bash version.

```bash
docker build --tag uptime-monitor .
docker run uptime-monitor
```

## Tools used

- Linux (Linux Mint)
- Python 3 (requests)
- Bash and curl
- cron
- Git and GitHub
- Docker

## Roadmap

- [x] Bash script that checks websites
- [x] Automatic checks with cron and a log file
- [x] Version control with Git and GitHub
- [x] Docker container
- [x] Python version with error handling and timeouts
- [ ] Docker image for the Python version
- [ ] CI/CD with GitHub Actions
- [ ] Web page with the results
- [ ] Deploy to AWS with Terraform
- [ ] Monitoring with Prometheus and Grafana

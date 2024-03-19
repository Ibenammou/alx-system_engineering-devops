# 0x0C. Web server

**DevOpsSysAdmin**

- **By:** Sylvain Kalache
- **Weight:** 1
- **Project will start:** Feb 26, 2024 4:00 AM, must end by Feb 28, 2024 4:00 AM
- **Checker was released at:** Feb 26, 2024 4:00 PM
- **An auto review will be launched at the deadline**

## Concepts

For this project, we expect you to look at this concept:

- What is a Child Process?

## Background Context

In this project, some of the tasks will be graded on 2 aspects:

- Is your web-01 server configured according to requirements
- Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:

```bash

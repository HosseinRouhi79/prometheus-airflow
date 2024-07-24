# Airflow with Monitoring - Docker Compose Setup

This project provides a Docker Compose setup for running Apache Airflow with Prometheus and StatsD exporter for monitoring.

![image](https://github.com/user-attachments/assets/00e34e94-ac6f-48bf-8016-3f09daf4ba58)


## Setting Up
### Configuration Adjustments
Before starting the services, make some configuration changes to ensure proper operation with your environment.

Prometheus Target
Open the prometheus.yml file and locate the line:

`targets: ['192.168.59.133:9102']`

Replace 192.168.59.133 with the IP address of your machine running the StatsD exporter. Do not change the port (9102).

Airflow StatsD Integration
Navigate to the config folder and open the airflow.cfg file. Locate the following section:
```
[metrics]
# StatsD (https://github.com/etsy/statsd) integration settings.
# Enables sending metrics to StatsD. Make sure you change the port from 8125 to 9125
statsd_on = True
statsd_host = 192.168.59.133
statsd_port = 9125
statsd_prefix = airflow
```
Replace 192.168.59.133 with the IP address of your machine running the StatsD exporter.

### Start the Services
After making the configuration changes, run the following command to start all the services (Airflow, Prometheus, and StatsD exporter) defined in the docker-compose.yml file:

`docker-compose up -d`

## Using Airflow
Airflow Web UI: Access the Airflow web interface at http://<your_host_ip>:8080.

Default username: airflow
Default password: airflow (Change this for production!)
Creating DAGs: Create DAG (Directed Acyclic Graph) files defining your workflows within the dags directory.

![image](https://github.com/user-attachments/assets/353e341f-4948-4e65-bbe2-6f7122afb3cd)

Monitoring with Prometheus
Prometheus UI: Access the Prometheus web interface at http://<your_host_ip>:9090.

StatsD Integration: The StatsD exporter collects metrics from Airflow tasks and exposes them to Prometheus for scraping.

![image](https://github.com/user-attachments/assets/2577d4f3-906f-4661-a554-7b297d3fbcff)

### Grafana
For improved visualization, consider using Grafana. Start by creating a Grafana container with the following command:
`docker run -d -p 3000:3000 --name=grafana grafana/grafana-enterprise`

![image](https://github.com/user-attachments/assets/6fb25901-eacd-49bf-9348-2ce71abb66f8)


### Additional Notes
This is a basic setup for development and testing. You might need to adjust configurations for production environments.
Consider customizing the docker-compose.yml file to specify environment variables, network configurations, or additional services.
Refer to the official documentation for Airflow, Prometheus, and StatsD exporter for further configuration options.
### Contributing
Feel free to contribute to this project by creating pull requests on GitHub.



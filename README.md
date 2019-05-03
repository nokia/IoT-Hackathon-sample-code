# IoT-Hackathon-sample-code

This repository provides examples and instructions for the participants of Nokia challenge in [Iothon 2019](https://iothon.io/).

## Challenge

The challenge is to create example demos of new digital services and business opportunities made possible by LuxTurrim5G and μMEC, for a real smart city. The teams are encouraged to come up with services and/or APIs that they consider beneficial as additions to the mobile network, to support the new digital service.

The following aspects are valued when choosing the winner:
1. Freshness of idea
2. Feasibility: Theoretical plan + Practical demo
3. Added value for a smart city citizen, for example: Practical help, Improved safety, Information, Experience (visual, audio, etc.)
4. Productization: can it be made into a commercial product

## Setup

During the challenge, the LuxTurrim5G and μMEC devices are emulated with Raspberry Pis and Nokia IoT Connectors. Some of the Raspberry Pis and all of the Nokia IoT Connectors are pre-configured, to kickstart the hacking process.

The pre-configured sensor devices, Raspberry Pis and Nokia IoT Connectors, are set to read data from the sensors and to push it to an InfluxDB instance. For quick instructions on how to access InfluxDB see [How to access an InfluxDB](instructions/How_to_access_InfluxDB.md) under `instructions/`.

In addition to Raspberry Pi, for which there are plenty of instructions publicly available, there are five Nokia IoT Connectors pre-configured to listen Ruuvi sensors tags and to push the data from them to the InfluxDB. See [airsense](instructions/airsense.txt) under `instructions/` for concise instructions on how to get started with those.

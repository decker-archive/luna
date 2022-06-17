![](./luna-repobrand.png)

# Luna

Welcome to Luna, Venera's Notification System.

If you want to get development updates, ask questions or get support you can contact us via our Discord Server or IRC Channel.

- Discord: [discord.gg/V7n95jcX2U](https://discord.gg/V7n95jcX2U).
- IRC Channel: #venera on irc.libera.chat.

# Design Document

Luna uses Python with aiohttp scaling on a node using gunicorn and redis.

Luna is not an alternative to vulcan, it only transmits events from it.

## Receiving Events

Luna receives events from vulcan using redis pubsub, in the future we may use another more scalable system.

## Interaction

Luna is only really made to transmit events. The little interaction that there will be are gonna be small things, like changing your status.

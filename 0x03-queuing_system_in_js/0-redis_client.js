import { createClient } from "redis";

async function RedisConnect() {
  const client = createClient();
  client.on("error", (err) =>
    console.log("Redis client not connected to the server:", err)
  );
  client.on("connect", () => {
    console.log("Redis client connected to the server");
  });
  const connection = await client.connect();
  return connection;
}

async function main() {
  const connection = await RedisConnect();
}

main();

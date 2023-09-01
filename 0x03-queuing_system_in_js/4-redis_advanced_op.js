#!/usr/bin/env node

import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');

  // Create Hash
  client.hset(
    'HolbertonSchools',
    'Portland',
    50,
    (err, reply1) => {
      if (err) {
        console.error('Error creating hash:', err);
      } else {
        console.log('Reply:', 1);
      }
    }
  );

  client.hset(
    'HolbertonSchools',
    'Seattle',
    80,
    (err, reply2) => {
      if (err) {
        console.error('Error creating hash:', err);
      } else {
        console.log('Reply:', 1);
      }
    }
  );

  client.hset(
    'HolbertonSchools',
    'New York',
    20,
    (err, reply3) => {
      if (err) {
        console.error('Error creating hash:', err);
      } else {
        console.log('Reply:', 1);
      }
    }
  );

  client.hset(
    'HolbertonSchools',
    'Bogota',
    20,
    (err, reply4) => {
      if (err) {
        console.error('Error creating hash:', err);
      } else {
        console.log('Reply:', 1);
      }
    }
  );

  client.hset(
    'HolbertonSchools',
    'Cali',
    40,
    (err, reply5) => {
      if (err) {
        console.error('Error creating hash:', err);
      } else {
        console.log('Reply:', 1);
      }
    }
  );

  client.hset(
    'HolbertonSchools',
    'Paris',
    2,
    (err, reply6) => {
      if (err) {
        console.error('Error creating hash:', err);
      } else {
        console.log('Reply:', 1);
      }
    }
  );

  // Display Hash
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.error('Error retrieving hash:', err);
    } else {
      console.log(reply);
    }

    // Close the Redis connection
    client.quit();
  });
});

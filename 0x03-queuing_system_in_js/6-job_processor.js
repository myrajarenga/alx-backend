#!/usr/bin/env node
import { createQueue } from 'kue';
const kue = require('kue');
const queue = kue.createQueue();

// Function to send notifications
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs in the 'push_notification_code' queue
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function with the job data
  sendNotification(phoneNumber, message);

  // Mark the job as completed
  done();
});

// Handle errors
queue.on('error', (err) => {
  console.error('Kue queue error:', err);
});

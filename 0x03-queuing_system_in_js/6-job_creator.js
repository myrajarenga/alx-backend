#!/usr/bin/env node
import { createQueue } from 'kue';
const kue = require('kue');

// Create a Kue queue
const queue = kue.createQueue();

// Object containing job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a test message',
};

// Create a job in the 'push_notification_code' queue
const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.error('Error creating job:', err);
  }
});

// Listen for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Listen for job failure
job.on('failed', () => {
  console.error('Notification job failed');
});


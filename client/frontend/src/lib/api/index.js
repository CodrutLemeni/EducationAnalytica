import axios from 'axios';

const API = axios.create({
  validateStatus: () => true,
});

export default API;
export * from './convert';

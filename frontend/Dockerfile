FROM node:20-alpine
WORKDIR /app
COPY package.json tsconfig.json next.config.mjs next-env.d.ts ./
COPY app ./app
COPY lib ./lib
RUN npm install
RUN npm run build
CMD ["npm", "run", "start"]

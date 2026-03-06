FROM node:20-alpine AS builder
WORKDIR /app

COPY package.json tsconfig.json next.config.mjs next-env.d.ts ./
COPY app ./app
COPY components ./components
COPY lib ./lib

RUN npm install
RUN npm run build

FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production \
    NEXT_TELEMETRY_DISABLED=1

COPY --from=builder /app .

CMD ["npm", "run", "start"]

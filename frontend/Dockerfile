FROM node:18-alpine

WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install

COPY . .

RUN yarn build

# Expose Vite's default dev server port
EXPOSE 5173

# Run the development server, binding to 0.0.0.0
CMD ["yarn", "dev", "--host"]


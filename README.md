# NoDoubtEstate

Flash launch product under Pay Dirt Global LLC  
Entry-level ebook-style estate planning with crypto and pet options.

## Features
- $32 digital will (watermarked preview)  
- $40 option includes Polygon notarization  
- Zero-data-retention model  
- Crypto payments supported (Stripe + Coinbase Commerce planned)

## Deployment
- Frontend: Vercel (/frontend)  
- Backend: Render or Vercel API routes (/backend)  
- Domain: NoDoubtEstate.com

## Environment Variables

| Variable | Usage | Environment |
| --- | --- | --- |
| `EMAIL_SMTP_HOST` | Outgoing email server for sending messages | Backend |
| `EMAIL_IMAP_HOST` | Incoming email server for monitoring replies | Backend |
| `EMAIL_ADDRESS` | Email account used by the service | Backend |
| `EMAIL_PASSWORD` | Password or app password for `EMAIL_ADDRESS` | Backend |
| `OPENAI_API_KEY` | Access key for OpenAI-powered features | Backend |
| `GITHUB_TOKEN` | GitHub access for automation scripts | Backend |
| `VERCEL_TOKEN` | Deploy frontend to Vercel | Frontend |

# HTTPS and Secure Configuration

## Settings Implemented

### SSL/HTTPS Enforcement
- SECURE_SSL_REDIRECT = True: All HTTP requests redirect to HTTPS
- SECURE_HSTS_SECONDS = 31536000: Browser remembers to use HTTPS for 1 year
- SECURE_HSTS_INCLUDE_SUBDOMAINS = True: Apply to all subdomains
- SECURE_HSTS_PRELOAD = True: Allow browser preloading

### Secure Cookies
- SESSION_COOKIE_SECURE = True: Session cookies only via HTTPS
- CSRF_COOKIE_SECURE = True: CSRF cookies only via HTTPS

### Security Headers
- X_FRAME_OPTIONS = DENY: Prevent clickjacking
- SECURE_CONTENT_TYPE_NOSNIFF = True: Prevent MIME-sniffing
- SECURE_BROWSER_XSS_FILTER = True: Enable XSS protection

## Deployment Notes

For production deployment:
1. Obtain SSL certificate
2. Configure web server for HTTPS
3. Ensure all settings above are enabled
4. Test with SSL Labs

## Development
For local testing, temporarily set:
- SECURE_SSL_REDIRECT = False
- SESSION_COOKIE_SECURE = False
- CSRF_COOKIE_SECURE = False
EOF
FROM python:3.11-slim

WORKDIR /frontend

COPY pyproject.toml .
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && pip install uv \
    # && uv pip compile pyproject.toml -o requirements.txt \
    # && uv pip install --system -r requirements.txt \
    # && rm requirements.txt \
    && apt-get remove -y gcc libpq-dev \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*


RUN useradd -m appuser \
    && chown -R appuser:appuser /frontend
    
USER appuser

# Copy the rest of the files as appuser
COPY --chown=appuser:appuser . .

# Set environment variables
ENV PORT=8050
ENV PYTHONPATH=/frontend/src

# Expose port
EXPOSE 8050

CMD ["uv", "run", "src/app.py"]

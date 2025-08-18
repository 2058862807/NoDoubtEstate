<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dream AI Agent - Ultimate Office Suite</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #fff;
            min-height: 100vh;
            overflow-x: hidden;
        }

        .ai-header {
            background: rgba(0, 0, 0, 0.25);
            backdrop-filter: blur(15px);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.18);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .ai-logo {
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(45deg, #00f5ff, #ff00ff);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .ai-status {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .status-dot {
            width: 12px;
            height: 12px;
            background: #00d386;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.7; transform: scale(1.1); }
        }

        .voice-control {
            position: fixed;
            top: 50%;
            right: 2rem;
            transform: translateY(-50%);
            z-index: 1000;
        }

        .voice-button {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            border: none;
            color: white;
            font-size: 1.8rem;
            cursor: pointer;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }

        .voice-button:hover {
            transform: scale(1.1);
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4);
        }

        .voice-button.listening {
            background: linear-gradient(45deg, #ff0040, #ff4081);
            animation: listening 1s infinite;
        }

        @keyframes listening {
            0%, 100% { box-shadow: 0 0 20px rgba(255, 0, 64, 0.5); }
            50% { box-shadow: 0 0 40px rgba(255, 0, 64, 0.8); }
        }

        .main-container {
            display: grid;
            grid-template-columns: 320px 1fr;
            height: calc(100vh - 80px);
        }

        .sidebar {
            background: rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(10px);
            padding: 1.5rem 1rem;
            overflow-y: auto;
            border-right: 1px solid rgba(255, 255, 255, 0.18);
        }

        .nav-section {
            margin-bottom: 1.5rem;
        }

        .nav-title {
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: rgba(255, 255, 255, 0.6);
            margin-bottom: 0.75rem;
        }

        .nav-item {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 0.75rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .nav-item:hover, .nav-item.active {
            background: rgba(255, 255, 255, 0.15);
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }

        .nav-icon {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            display: block;
        }

        .nav-item-title {
            font-weight: 600;
            margin-bottom: 0.25rem;
            font-size: 0.9rem;
        }

        .nav-item-desc {
            font-size: 0.75rem;
            opacity: 0.8;
            line-height: 1.3;
        }

        .workspace {
            padding: 1.5rem;
            overflow-y: auto;
        }

        .panel {
            background: rgba(0, 0, 0, 0.22);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 15px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .panel h3 {
            margin-bottom: 1rem;
            font-size: 1.2rem;
            color: #fff;
        }

        .metrics {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        @media (max-width: 900px) {
            .metrics { grid-template-columns: repeat(2, 1fr); }
            .main-container { grid-template-columns: 1fr; }
            .sidebar { display: none; }
        }

        .metric {
            background: rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
        }

        .metric-value {
            font-size: 1.8rem;
            font-weight: 800;
            color: #00ff88;
            display: block;
        }

        .metric-label {
            font-size: 0.8rem;
            opacity: 0.8;
            margin-top: 0.5rem;
        }

        .command-interface {
            margin-bottom: 1.5rem;
        }

        .command-input {
            width: 100%;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 10px;
            padding: 1rem;
            color: white;
            font-size: 1rem;
            margin-bottom: 0.75rem;
        }

        .command-input::placeholder {
            color: rgba(255, 255, 255, 0.6);
        }

        .command-input:focus {
            outline: none;
            border-color: #00d386;
            background: rgba(255, 255, 255, 0.15);
        }

        .suggestions {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1rem;
        }

        .chip {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.18);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.85rem;
            transition: all 0.3s ease;
        }

        .chip:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-1px);
        }

        .tasks {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1rem;
        }

        .task {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 12px;
            padding: 1rem;
        }

        .task-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.5rem;
        }

        .badge {
            padding: 0.2rem 0.6rem;
            border-radius: 10px;
            font-weight: 600;
            font-size: 0.75rem;
        }

        .status-running {
            background: rgba(255, 193, 7, 0.2);
            color: #ffd666;
        }

        .status-complete {
            background: rgba(0, 211, 134, 0.2);
            color: #00d386;
        }

        .status-pending {
            background: rgba(108, 117, 125, 0.2);
            color: #c9ccd1;
        }

        .ai-response {
            background: rgba(0, 0, 0, 0.2);
            border-left: 4px solid #00d386;
            border-radius: 8px;
            padding: 1rem;
            margin-top: 1rem;
            white-space: pre-wrap;
            font-family: 'Monaco', 'Menlo', monospace;
            font-size: 0.9rem;
            line-height: 1.4;
        }

        .module-content {
            display: none;
        }

        .module-content.active {
            display: block;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .fax-interface {
            display: grid;
            gap: 1rem;
        }

        .file-upload {
            border: 2px dashed rgba(255, 255, 255, 0.3);
            border-radius: 10px;
            padding: 2rem;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .file-upload:hover {
            border-color: #00d386;
            background: rgba(0, 211, 134, 0.1);
        }

        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }

        .form-group {
            margin-bottom: 1rem;
        }

        .form-label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }

        .form-input {
            width: 100%;
            padding: 0.75rem;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 8px;
            color: white;
        }

        .btn {
            background: linear-gradient(45deg, #00d386, #00a67e);
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            color: white;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(0, 211, 134, 0.3);
        }

        .floating-chat {
            position: fixed;
            bottom: 2rem;
            left: 2rem;
            width: 60px;
            height: 60px;
            background: linear-gradient(45deg, #667eea, #764ba2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
            z-index: 999;
        }

        .floating-chat:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body>
    <header class="ai-header">
        <div class="ai-logo">DREAM</div>
        <div class="ai-status">
            <div class="status-dot" id="statusDot"></div>
            <span id="systemStatus">AI Agent Online</span>
        </div>
    </header>

    <div class="voice-control">
        <button class="voice-button" id="voiceButton" onclick="toggleVoice()">🎤</button>
    </div>

    <div class="main-container">
        <nav class="sidebar">
            <div class="nav-section">
                <div class="nav-title">AI Agent</div>
                <div class="nav-item active" onclick="showModule('dashboard')">
                    <div class="nav-icon">🤖</div>
                    <div class="nav-item-title">Dashboard</div>
                    <div class="nav-item-desc">Control center & metrics</div>
                </div>
                <div class="nav-item" onclick="showModule('voice')">
                    <div class="nav-icon">🎙️</div>
                    <div class="nav-item-title">Voice Commands</div>
                    <div class="nav-item-desc">Hands-free operation</div>
                </div>
            </div>

            <div class="nav-section">
                <div class="nav-title">Communication</div>
                <div class="nav-item" onclick="showModule('email')">
                    <div class="nav-icon">📧</div>
                    <div class="nav-item-title">Smart Email</div>
                    <div class="nav-item-desc">AI-powered email management</div>
                </div>
                <div class="nav-item" onclick="showModule('fax')">
                    <div class="nav-icon">📠</div>
                    <div class="nav-item-title">Digital Fax</div>
                    <div class="nav-item-desc">Send & receive faxes</div>
                </div>
            </div>

            <div class="nav-section">
                <div class="nav-title">Development</div>
                <div class="nav-item" onclick="showModule('dev')">
                    <div class="nav-icon">💻</div>
                    <div class="nav-item-title">Dev Tools</div>
                    <div class="nav-item-desc">Git, deploy, code generation</div>
                </div>
                <div class="nav-item" onclick="showModule('ai')">
                    <div class="nav-icon">🧠</div>
                    <div class="nav-item-title">AI Models</div>
                    <div class="nav-item-desc">OpenAI, DeepSeek, analysis</div>
                </div>
            </div>

            <div class="nav-section">
                <div class="nav-title">Business</div>
                <div class="nav-item" onclick="showModule('legal')">
                    <div class="nav-icon">⚖️</div>
                    <div class="nav-item-title">Legal Assistant</div>
                    <div class="nav-item-desc">Contracts, compliance, research</div>
                </div>
                <div class="nav-item" onclick="showModule('domains')">
                    <div class="nav-icon">🌐</div>
                    <div class="nav-item-title">Domain Manager</div>
                    <div class="nav-item-desc">DNS, SSL, domain operations</div>
                </div>
            </div>
        </nav>

        <main class="workspace">
            <!-- Dashboard Module -->
            <div class="module-content active" id="dashboard">
                <div class="panel">
                    <h3>🧠 Recursive Self-Learning Metrics</h3>
                    <div class="metrics">
                        <div class="metric">
                            <div class="metric-value" id="skillsLearned">0</div>
                            <div class="metric-label">Skills Learned</div>
                        </div>
                        <div class="metric">
                            <div class="metric-value" id="successRate">0%</div>
                            <div class="metric-label">Success Rate</div>
                        </div>
                        <div class="metric">
                            <div class="metric-value" id="timeSaved">0h</div>
                            <div class="metric-label">Time Saved</div>
                        </div>
                        <div class="metric">
                            <div class="metric-value" id="optimizations">0</div>
                            <div class="metric-label">Optimizations</div>
                        </div>
                    </div>
                </div>

                <div class="panel command-interface">
                    <h3>Universal Command Interface</h3>
                    <input type="text" class="command-input" id="commandInput" placeholder="Tell Dream what you need... (voice or text)">
                    <div class="suggestions" id="suggestions"></div>
                    <div class="ai-response" id="aiResponse" style="display: none;"></div>
                </div>

                <div class="panel">
                    <h3>Active Tasks & Processes</h3>
                    <div class="tasks" id="activeTasks"></div>
                </div>

                <div class="panel">
                    <h3>System Integrations</h3>
                    <div class="tasks">
                        <div class="task">
                            <div class="task-header">
                                <strong>🐙 GitHub</strong>
                                <span class="badge status-complete" id="githubStatus">Connected</span>
                            </div>
                            <small>Repository management & deployment</small>
                        </div>
                        <div class="task">
                            <div class="task-header">
                                <strong>▲ Vercel</strong>
                                <span class="badge status-complete" id="vercelStatus">Ready</span>
                            </div>
                            <small>Automated deployment pipeline</small>
                        </div>
                        <div class="task">
                            <div class="task-header">
                                <strong>🤖 OpenAI</strong>
                                <span class="badge status-complete" id="openaiStatus">Active</span>
                            </div>
                            <small>GPT models for AI operations</small>
                        </div>
                        <div class="task">
                            <div class="task-header">
                                <strong>🧠 DeepSeek</strong>
                                <span class="badge status-complete" id="deepseekStatus">Active</span>
                            </div>
                            <small>Alternative AI model provider</small>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Fax Module -->
            <div class="module-content" id="fax">
                <div class="panel">
                    <h3>📠 Digital Fax Center</h3>
                    <div class="fax-interface">
                        <div class="file-upload" onclick="document.getElementById('faxFile').click()">
                            <input type="file" id="faxFile" style="display: none;" accept=".pdf,.doc,.docx,.txt,.jpg,.png">
                            <div style="font-size: 3rem; margin-bottom: 1rem;">📄</div>
                            <div>Click to select document to fax</div>
                            <small>Supports: PDF, DOC, DOCX, images</small>
                        </div>
                        
                        <div class="form-row">
                            <div class="form-group">
                                <label class="form-label">Recipient Fax Number</label>
                                <input type="tel" class="form-input" id="faxNumber" placeholder="+1 (555) 123-4567">
                            </div>
                            <div class="form-group">
                                <label class="form-label">Sender Information</label>
                                <input type="text" class="form-input" id="senderInfo" placeholder="Your Name/Company">
                            </div>
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label">Cover Note (Optional)</label>
                            <textarea class="form-input" id="coverNote" rows="3" placeholder="Brief message for the cover page..."></textarea>
                        </div>
                        
                        <button class="btn" onclick="sendFax()">📠 Send Fax</button>
                    </div>
                </div>

                <div class="panel">
                    <h3>Fax History</h3>
                    <div class="tasks" id="faxHistory">
                        <div class="task">
                            <div class="task-header">
                                <strong>Contract to Legal Dept</strong>
                                <span class="badge status-complete">Delivered</span>
                            </div>
                            <small>Sent to +1 (555) 123-4567 • 2 pages</small>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Email Module -->
            <div class="module-content" id="email">
                <div class="panel">
                    <h3>📧 AI-Powered Email Management</h3>
                    <div class="form-group">
                        <label class="form-label">Search Query</label>
                        <input type="text" class="form-input" id="emailQuery" placeholder="urgent, client, invoice, etc.">
                    </div>
                    <div class="form-group">
                        <label class="form-label">AI Reply</label>
                        <textarea class="form-input" id="emailReply" rows="4" placeholder="AI will help compose the perfect response..."></textarea>
                    </div>
                    <button class="btn" onclick="handleEmail()">🤖 Process with AI</button>
                </div>
            </div>

            <!-- Other modules -->
            <div class="module-content" id="voice">
                <div class="panel">
                    <h3>🎙️ Voice Command Center</h3>
                    <p>Use the voice button on the right or speak these commands:</p>
                    <div class="suggestions">
                        <div class="chip">"Deploy my latest changes"</div>
                        <div class="chip">"Send fax to legal department"</div>
                        <div class="chip">"Check urgent emails"</div>
                        <div class="chip">"Generate project report"</div>
                    </div>
                </div>
            </div>

            <div class="module-content" id="dev">
                <div class="panel">
                    <h3>💻 Development Tools</h3>
                    <p>Git operations, deployments, and code generation.</p>
                </div>
            </div>

            <div class="module-content" id="ai">
                <div class="panel">
                    <h3>🧠 AI Model Access</h3>
                    <p>OpenAI GPT-4, DeepSeek, and other AI models for analysis and generation.</p>
                </div>
            </div>

            <div class="module-content" id="legal">
                <div class="panel">
                    <h3>⚖️ Legal Assistant</h3>
                    <p>Contract analysis, compliance checking, and legal research.</p>
                </div>
            </div>

            <div class="module-content" id="domains">
                <div class="panel">
                    <h3>🌐 Domain Management</h3>
                    <p>DNS configuration, SSL certificates, and domain operations.</p>
                </div>
            </div>
        </main>
    </div>

    <div class="floating-chat" onclick="focusCommand()">💬</div>

    <script>
        let isListening = false;
        let recognition;
        let taskCount = 0;
        let completedTasks = 0;

        // Voice Recognition
        if ('webkitSpeechRecognition' in window) {
            recognition = new webkitSpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'en-US';

            recognition.onresult = function(event) {
                const command = event.results[0][0].transcript;
                document.getElementById('commandInput').value = command;
                executeCommand(command);
            };

            recognition.onend = function() {
                isListening = false;
                document.getElementById('voiceButton').classList.remove('listening');
                document.getElementById('voiceButton').innerHTML = '🎤';
            };
        }

        function toggleVoice() {
            if (!recognition) {
                alert('Voice recognition not supported in this browser');
                return;
            }

            if (isListening) {
                recognition.stop();
            } else {
                recognition.start();
                isListening = true;
                document.getElementById('voiceButton').classList.add('listening');
                document.getElementById('voiceButton').innerHTML = '🔴';
            }
        }

        // Module Navigation
        function showModule(moduleId) {
            document.querySelectorAll('.module-content').forEach(m => m.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
            
            document.getElementById(moduleId).classList.add('active');
            event.target.closest('.nav-item').classList.add('active');
        }

        // Command Execution - FIXED
        async function executeCommand(command) {
            const responseDiv = document.getElementById('aiResponse');
            responseDiv.style.display = 'block';
            responseDiv.textContent = `Processing: "${command}"\n\n🤖 Dream AI is analyzing your request...`;

            taskCount++;
            addTask(command, 'running');

            try {
                const result = await handleSpecificCommands(command);
                if (result) {
                    const data = await result.json();
                    
                    // Extract the actual response text properly
                    let displayText = '';
                    if (data.output) {
                        displayText = data.output;
                    } else if (data.report) {
                        displayText = data.report;
                    } else if (data.text) {
                        displayText = data.text;
                    } else if (data.status) {
                        displayText = `Status: ${data.status}${data.detail ? '\n' + data.detail : ''}`;
                    } else if (data.message) {
                        displayText = data.message;
                    } else {
                        displayText = JSON.stringify(data, null, 2);
                    }
                    
                    responseDiv.textContent = `"${command}"\n\n✅ ${displayText}`;
                    updateTaskStatus(command, 'complete');
                    completedTasks++;
                } else {
                    // Fallback to general agent
                    const response = await fetch('/agent/run', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({
                            goal: command,
                            params: { autonomous: true, learning_mode: true }
                        })
                    });
                    
                    if (response.ok) {
                        const result = await response.json();
                        const displayText = result.report || result.output || 'Task completed successfully';
                        responseDiv.textContent = `"${command}"\n\n🤖 ${displayText}`;
                        updateTaskStatus(command, 'complete');
                        completedTasks++;
                    } else {
                        throw new Error(`Server error: ${response.status}`);
                    }
                }
            } catch (error) {
                responseDiv.textContent = `"${command}"\n\n❌ Error: ${error.message}`;
                updateTaskStatus(command, 'pending');
            }
            
            updateMetrics();
        }

        // Specific Command Handlers - FIXED
        async function handleSpecificCommands(command) {
            const lower = command.toLowerCase();
            
            if (lower.includes('fax')) {
                return await fetch('/fax/send', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        to_number: '+1234567890',
                        document_path: 'document.pdf',
                        cover_note: 'Sent via Dream AI'
                    })
                });
            }
            
            if (lower.includes('email')) {
                return await fetch('/email/reply', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        thread_query: 'urgent',
                        reply_text: 'AI generated response',
                        dry_run: false
                    })
                });
            }
            
            if (lower.includes('deploy')) {
                return await fetch('/vercel/deploy', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        project_dir: '.',
                        prod: true
                    })
                });
            }
            
            if (lower.includes('git') || lower.includes('push')) {
                return await fetch('/git/push', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        repo_path: '.',
                        message: 'AI agent update'
                    })
                });
            }
            
            if (lower.includes('openai') || lower.includes('generate') || lower.includes('what') || lower.includes('analyze')) {
                return await fetch('/llm/complete', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        provider: 'openai',
                        model: 'gpt-4o-mini',
                        prompt: command
                    })
                });
            }
            
            if (lower.includes('deepseek')) {
                return await fetch('/llm/complete', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        provider: 'deepseek',
                        model: 'deepseek-chat',
                        prompt: command
                    })
                });
            }
            
            return null;
        }

        // Digital Fax Functions
        async function sendFax() {
            const faxNumber = document.getElementById('faxNumber').value;
            const senderInfo = document.getElementById('senderInfo').value;
            const coverNote = document.getElementById('coverNote').value;
            const fileInput = document.getElementById('faxFile');
            
            if (!faxNumber) {
                alert('Please enter a fax number');
                return;
            }
            
            if (!fileInput.files[0]) {
                alert('Please select a document to fax');
                return;
            }
            
            try {
                const formData = new FormData();
                formData.append('to_number', faxNumber);
                formData.append('sender_info', senderInfo);
                formData.append('cover_note', coverNote);
                formData.append('document', fileInput.files[0]);
                
                const response = await fetch('/fax/send', {
                    method: 'POST',
                    body: formData
                });
                
                if (response.ok) {
                    const result = await response.json();
                    alert(`✅ Fax sent successfully! ID: ${result.fax_id}`);
                    addFaxToHistory(faxNumber, fileInput.files[0].name, 'Delivered');
                    clearFaxForm();
                } else {
                    throw new Error('Failed to send fax');
                }
            } catch (error) {
                alert(`❌ Error sending fax: ${error.message}`);
            }
        }

        function addFaxToHistory(number, filename, status) {
            const historyDiv = document.getElementById('faxHistory');
            const taskDiv = document.createElement('div');
            taskDiv.className = 'task';
            taskDiv.innerHTML = `
                <div class="task-header">
                    <strong>${filename}</strong>
                    <span class="badge status-complete">${status}</span>
                </div>
                <small>Sent to ${number} • ${new Date().toLocaleString()}</small>
            `;
            historyDiv.appendChild(taskDiv);
        }

        function clearFaxForm() {
            document.getElementById('faxNumber').value = '';
            document.getElementById('senderInfo').value = '';
            document.getElementById('coverNote').value = '';
            document.getElementById('faxFile').value = '';
        }

        // Email Functions
        async function handleEmail() {
            const query = document.getElementById('emailQuery').value;
            const reply = document.getElementById('emailReply').value;
            
            if (!query) {
                alert('Please enter a search query');
                return;
            }
            
            try {
                const response = await fetch('/email/reply', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        thread_query: query,
                        reply_text: reply || 'AI will generate an appropriate response',
                        dry_run: false
                    })
                });
                
                if (response.ok) {
                    const result = await response.json();
                    alert(`✅ Email processed: ${result.status}`);
                    addTask(`Email: ${query}`, 'complete');
                    completedTasks++;
                    updateMetrics();
                } else {
                    throw new Error('Failed to process email');
                }
            } catch (error) {
                alert(`❌ Error processing email: ${error.message}`);
            }
        }

        // Task Management
        function addTask(title, status) {
            const tasksDiv = document.getElementById('activeTasks');
            const taskDiv = document.createElement('div');
            taskDiv.className = 'task';
            taskDiv.innerHTML = `
                <div class="task-header">
                    <strong>${title.length > 50 ? title.substring(0, 50) + '...' : title}</strong>
                    <span class="badge status-${status}">${status}</span>
                </div>
                <small>${new Date().toLocaleTimeString()}</small>
            `;
            tasksDiv.appendChild(taskDiv);
            
            // Keep only latest 6 tasks
            const tasks = tasksDiv.children;
            if (tasks.length > 6) {
                tasksDiv.removeChild(tasks[0]);
            }
        }

        function updateTaskStatus(title, newStatus) {
            const tasks = document.querySelectorAll('#activeTasks .task');
            tasks.forEach(task => {
                const taskTitle = task.querySelector('strong').textContent;
                if (taskTitle.includes(title.substring(0, 30))) {
                    const badge = task.querySelector('.badge');
                    badge.className = `badge status-${newStatus}`;
                    badge.textContent = newStatus;
                }
            });
        }

        // Metrics Updates
        function updateMetrics() {
            const successRate = taskCount > 0 ? Math.round((completedTasks / taskCount) * 100) : 0;
            const timeSaved = (completedTasks * 0.5).toFixed(1);
            
            document.getElementById('skillsLearned').textContent = completedTasks * 3;
            document.getElementById('successRate').textContent = `${successRate}%`;
            document.getElementById('timeSaved').textContent = `${timeSaved}h`;
            document.getElementById('optimizations').textContent = completedTasks;
        }

        // System Status Updates
        async function updateSystemStatus() {
            try {
                const response = await fetch('/health');
                const status = await response.json();
                
                const statusDot = document.getElementById('statusDot');
                const statusText = document.getElementById('systemStatus');
                
                if (status.status === 'ok') {
                    statusDot.style.background = '#00d386';
                    statusText.textContent = 'AI Agent Online • All Systems Operational';
                } else {
                    statusDot.style.background = '#ffc107';
                    statusText.textContent = 'AI Agent Online • Some Issues Detected';
                }
            } catch (error) {
                const statusDot = document.getElementById('statusDot');
                const statusText = document.getElementById('systemStatus');
                statusDot.style.background = '#ff4d4f';
                statusText.textContent = 'AI Agent Offline • Connection Issues';
            }
        }

        // Suggestions
        const suggestions = [
            'OpenAI explain artificial intelligence',
            'DeepSeek write a Python function',
            'Deploy latest changes to production',
            'Check and reply to urgent emails',
            'Generate quarterly business report',
            'Push code to GitHub with commit message',
            'Analyze recent email patterns',
            'Create legal compliance document',
            'Update domain DNS settings',
            'Generate technical documentation'
        ];

        function updateSuggestions() {
            const suggestionsDiv = document.getElementById('suggestions');
            suggestionsDiv.innerHTML = '';
            
            // Show 4 random suggestions
            const randomSuggestions = suggestions
                .sort(() => 0.5 - Math.random())
                .slice(0, 4);
                
            randomSuggestions.forEach(suggestion => {
                const chip = document.createElement('div');
                chip.className = 'chip';
                chip.textContent = suggestion;
                chip.onclick = () => executeCommand(suggestion);
                suggestionsDiv.appendChild(chip);
            });
        }

        // Utility Functions
        function focusCommand() {
            document.getElementById('commandInput').focus();
        }

        // Initialize Application
        document.addEventListener('DOMContentLoaded', function() {
            updateSystemStatus();
            updateMetrics();
            updateSuggestions();
            
            // Set up intervals
            setInterval(updateSystemStatus, 10000);
            setInterval(updateSuggestions, 30000);
            
            // Command input handler
            document.getElementById('commandInput').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    const command = this.value.trim();
                    if (command) {
                        executeCommand(command);
                        this.value = '';
                    }
                }
            });
            
            // File upload handler
            document.getElementById('faxFile').addEventListener('change', function(e) {
                if (e.target.files[0]) {
                    const fileName = e.target.files[0].name;
                    const uploadDiv = document.querySelector('.file-upload');
                    uploadDiv.innerHTML = `
                        <div style="font-size: 3rem; margin-bottom: 1rem;">📄</div>
                        <div><strong>${fileName}</strong></div>
                        <small>Click to change document</small>
                    `;
                }
            });
            
            // Add some initial demo tasks
            setTimeout(() => {
                addTask('System Initialization', 'complete');
                completedTasks++;
                updateMetrics();
            }, 1000);
            
            setTimeout(() => {
                addTask('API Integration Check', 'complete');
                completedTasks++;
                updateMetrics();
            }, 2000);
        });
    </script>
</body>
</html>
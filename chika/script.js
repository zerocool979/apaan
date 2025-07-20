// Impor pipeline dari Transformers.js
import { pipeline } from 'https://cdn.jsdelivr.net/npm/@xenova/transformers@2.17.1';

document.addEventListener('DOMContentLoaded', function() {

    // --- inisialisasi pipeline LLM ---
    let chikaGenerator = null;

    async function initLLM() {
        try {
            chikaGenerator = await pipeline('text-generation', 'Xenova/phi-1_5');
            console.log('✅ Model LLM Chika (phi-1.5) berhasil dimuat.');
        } catch (e) {
            console.error('❌ Gagal memuat model LLM:', e);
        }
    }

    // --- memproses transkrip → respons ---
    async function chikaRespondWithLLM(userText) {
        if (!chikaGenerator) {
            console.warn("Model LLM belum siap.");
            speakText("Maaf, saya belum siap menjawab.");
            return;
        }

        const systemPrompt = `
    Kamu adalah Chika, asisten suara personal yang lembut, perhatian, dan sedikit imut.
    Balaslah pengguna dengan nada ramah dan penuh empati dalam Bahasa Indonesia. Jangan terlalu kaku.
    `;

        const prompt = `${systemPrompt}\nPengguna: ${userText}\nChika:`;

        try {
            const output = await chikaGenerator(prompt, {
                max_new_tokens: 100,
                temperature: 0.7,
            });

            const chikaReply = output[0].generated_text.replace(prompt, '').trim();
            console.log("🧠 Chika menjawab:", chikaReply);
            speakText(chikaReply);

        } catch (err) {
            console.error("⚠️ Gagal menghasilkan respons dari LLM:", err);
            speakText("Maaf, saya tidak bisa menjawab sekarang.");
        }
    }



    initLLM(); // Panggil saat startup


    // --- Penanganan layar pemuatan ---
    const loadingScreen = document.getElementById('loading-screen');
    setTimeout(() => {
        loadingScreen.style.opacity = '0';
        // Sembunyikan setelah animasi selesai untuk mencegahnya memblokir interaksi
        setTimeout(() => {
            loadingScreen.style.display = 'none';
        }, 500); // Waktu ini seharusnya cocok dengan waktu transisi di CSS
    }, 1500); // Mulai memudar setelah 1,5 detik
    
    // Dapatkan elemen DOM yang dibutuhkan
    let video1 = document.getElementById('video1');
    let video2 = document.getElementById('video2');
    const micButton = document.getElementById('mic-button');
    const favorabilityBar = document.getElementById('favorability-bar');
    const floatingButton = document.getElementById('floating-button');
    const menuContainer = document.getElementById('menu-container');
    const menuItems = document.querySelectorAll('.menu-item');

    // --- Elemen Analisis Sentimen ---
    const sentimentInput = document.getElementById('sentiment-input');
    const analyzeButton = document.getElementById('analyze-button');
    const sentimentResult = document.getElementById('sentiment-result');

    let activeVideo = video1;
    let inactiveVideo = video2;

    // Daftar Video
    const videoList = [
        'asset/3D image.mp4',
        'asset/Sambil tersenyum, dia bergoyang anggun dari sisi ke sisi, dan setelah beberapa saat, dia meletakkan tangannya di dagunya dan terus tersenyum.mp4',
        'asset/chabi-lalu tersenyum dan bergoyang anggun dari sisi ke sisi.mp4',
        'asset/sorak-sorai.mp4',
        'asset/tari.mp4',
        'asset/negatif/Tangan berkacak pinggang, mulut terus bergumam, ekspresi sedikit marah.mp4'
    ];

    // Fungsi pembantu untuk mengelola pengalihan video
    function _transitionVideo(nextVideoSrc) {
        const currentVideoSrc = activeVideo.querySelector('source').getAttribute('src');
        if (nextVideoSrc === currentVideoSrc) return; // Hindari memutar video yang sama

        inactiveVideo.querySelector('source').setAttribute('src', nextVideoSrc);
        inactiveVideo.load();

        inactiveVideo.addEventListener('canplaythrough', function onCanPlayThrough() {
            inactiveVideo.removeEventListener('canplaythrough', onCanPlayThrough);
            activeVideo.pause();
            inactiveVideo.play().catch(error => console.error("Video play failed:", error));
            activeVideo.classList.remove('active');
            inactiveVideo.classList.add('active');
            [activeVideo, inactiveVideo] = [inactiveVideo, activeVideo];
            activeVideo.addEventListener('ended', switchVideo, { once: true }); // Ikat kembali acara 'ended'
        }, { once: true });
    }

    // --- Fungsi pemutaran cross-fade video ---
    function switchVideo() {
        // 1. Pilih video berikutnya
        const currentVideoSrc = activeVideo.querySelector('source').getAttribute('src');
        let nextVideoSrc = currentVideoSrc;
        while (nextVideoSrc === currentVideoSrc) {
            const randomIndex = Math.floor(Math.random() * videoList.length);
            nextVideoSrc = videoList[randomIndex];
        }
        _transitionVideo(nextVideoSrc);
    }

    // Startup awal
    activeVideo.addEventListener('ended', switchVideo, { once: true });

    // --- Fungsi Text-to-Speech (TTS) ---
    let selectedVoice = null;

    // Fungsi untuk mendapatkan dan memilih suara
    function setVoice() {
        const voices = window.speechSynthesis.getVoices();
        // Coba cari suara berbahasa Indonesia yang terdengar lebih lembut atau alami
        // Prioritaskan suara Bahasa Indonesia, lalu cari suara dengan nama yang menyiratkan kelembutan/feminin, atau suara default
        selectedVoice = voices.find(voice => 
            (voice.lang === 'id-ID' && (voice.name.includes('Google Bahasa Indonesia') || voice.name.includes('Female'))) || 
            (voice.lang === 'id-ID') || // Prioritaskan ID
            voice.name.includes('Female') || // Suara wanita seringkali lebih lembut
            voice.name.includes('Zira') || // Contoh suara yang mungkin terdengar lembut
            voice.name.includes('Microsoft Eva') // Contoh suara lain
        );
        
        if (!selectedVoice) {
            console.warn('Suara Bahasa Indonesia atau suara yang cocok tidak ditemukan, menggunakan suara default.');
            // Fallback ke suara default jika tidak ada yang ditemukan
            selectedVoice = voices.find(voice => voice.default);
        }
    }

    // Panggil setVoice saat suara tersedia (biasanya setelah DOMContentLoaded atau beberapa saat)
    // Event 'voiceschanged' dipicu ketika daftar suara tersedia atau berubah
    if (window.speechSynthesis.onvoiceschanged !== undefined) {
        window.speechSynthesis.onvoiceschanged = setVoice;
    }
    setVoice(); // Panggil sekali saat startup jika suara sudah dimuat

    // Fungsi untuk mencetak suara yang tersedia ke konsol (untuk debugging)
    function getAvailableVoices() {
        const voices = window.speechSynthesis.getVoices();
        console.log('Suara yang tersedia:');
        voices.forEach(voice => {
            console.log(`- Nama: ${voice.name}, Bahasa: ${voice.lang}, Default: ${voice.default}`);
        });
    }
    // Anda bisa memanggil ini di console browser untuk melihat daftar suara: getAvailableVoices();

    function speakText(text) {
        // Hentikan ucapan yang sedang berlangsung untuk mencegah tumpang tindih
        window.speechSynthesis.cancel(); 
        const utterance = new SpeechSynthesisUtterance(text);
        
        if (selectedVoice) {
            utterance.voice = selectedVoice;
        } else {
            // Coba lagi setVoice jika belum terpilih
            setVoice();
            if (selectedVoice) {
                utterance.voice = selectedVoice;
            }
        }

        // Atur kecepatan bicara (1.0 adalah normal)
        utterance.rate = 0.9; // Sedikit lebih lambat untuk kesan lembut
        // Atur pitch suara (1.0 adalah normal)
        utterance.pitch = 1.0; // Kembali ke pitch normal untuk suara yang lebih alami

        window.speechSynthesis.speak(utterance);
    }


    // --- Inti pengenalan ucapan ---
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    let recognition;

    // Periksa apakah browser mendukung pengenalan suara
    if (SpeechRecognition) {
        recognition = new SpeechRecognition();
        recognition.continuous = true; //Lanjutkan mengidentifikasi
        recognition.lang = 'id-ID'; // Atur bahasa ke bahasa Indonesia
        recognition.interimResults = true; // Dapatkan hasil sementara

        recognition.onresult = (event) => {
            const transcriptContainer = document.getElementById('transcript');
            let final_transcript = '';
            let interim_transcript = '';

            for (let i = event.resultIndex; i < event.results.length; ++i) {
                if (event.results[i].isFinal) {
                    final_transcript += event.results[i][0].transcript;
                } else {
                    interim_transcript += event.results[i][0].transcript;
                }
            }
            
            // Menampilkan hasil pengenalan akhir
            transcriptContainer.textContent = final_transcript || interim_transcript;
            
            // Analisis sentimen dan peralihan video berdasarkan kata kunci
            if (final_transcript) {
                analyzeAndReact(final_transcript);
            }
        };

        recognition.onerror = (event) => {
            console.error('Kesalahan pengenalan ucapan:', event.error);
        };

    } else {
        console.log('Peramban Anda tidak mendukung pengenalan suara.');
        // Anda dapat memberikan perintah kepada pengguna di antarmuka
    }

    // --- Interaksi tombol mikrofon ---
    let isListening = false;

    micButton.addEventListener('click', function() {
        if (!SpeechRecognition) return; // Jika tidak didukung, jangan lakukan apa pun

        isListening = !isListening;
        micButton.classList.toggle('is-listening', isListening);
        const transcriptContainer = document.querySelector('.transcript-container');
        const transcriptText = document.getElementById('transcript');

        if (isListening) {
            transcriptText.textContent = 'Mendengarkan...'; // Tampilkan perintah segera
            transcriptContainer.classList.add('visible');
            recognition.start();
        } else {
            recognition.stop();
            transcriptContainer.classList.remove('visible');
            transcriptText.textContent = ''; // Hapus teks
        }
    });


    // --- Interaksi tombol mengambang ---
    floatingButton.addEventListener('click', (event) => {
        event.stopPropagation(); // Mencegah peristiwa muncul di dokumen
        menuContainer.classList.toggle('hidden');
    });

    menuItems.forEach(item => {
        item.addEventListener('click', function() {
            const videoSrc = this.getAttribute('data-video');
            playSpecificVideo(videoSrc);
            menuContainer.classList.add('hidden');
        });
    });

    // Klik di luar menu untuk menutup menu
    document.addEventListener('click', () => {
        if (!menuContainer.classList.contains('hidden')) {
            menuContainer.classList.add('hidden');
        }
    });

    // Cegah acara klik menu itu sendiri agar tidak menggelembung
    menuContainer.addEventListener('click', (event) => {
        event.stopPropagation();
    });


    function playSpecificVideo(videoSrc) {
        _transitionVideo(videoSrc);
    }

    // --- Analisis Sentimen dan Respon ---
    const positiveWords = ['senang', 'gembira', 'suka', 'hebat', 'halo', 'cantik'];
    const negativeWords = ['sedih', 'marah', 'benci', 'patah hati'];

    const positiveVideos = [
        'asset/chabi-lalu tersenyum dan bergoyang anggun dari sisi ke sisi.mp4',
        'asset/Sambil tersenyum, dia bergoyang anggun dari sisi ke sisi, dan setelah beberapa saat, dia meletakkan tangannya di dagunya dan terus tersenyum.mp4',
        'asset/sorak-sorai.mp4',
        'asset/tari.mp4'
    ];
    const negativeVideo = 'asset/negatif/Tangan berkacak pinggang, mulut terus bergumam, ekspresi sedikit marah.mp4';

    // Fungsi yang menganalisis teks dan bereaksi (termasuk respons suara)
    function analyzeAndReact(text) {
        let reaction = 'neutral'; // Defaultnya netral
        let responseText = 'Saya tidak yakin bagaimana perasaan Anda.'; // Respons default

        if (positiveWords.some(word => text.includes(word))) {
            reaction = 'positive';
            responseText = 'Wah, saya senang mendengarnya!';
        } else if (negativeWords.some(word => text.includes(word))) {
            reaction = 'negative';
            responseText = 'Oh, saya turut prihatin.';
        }

        if (reaction !== 'neutral') {
            switchVideoByEmotion(reaction);
        }
        speakText(responseText); // Chika merespons dengan suara
    }


    // --- Analisis sentimen model lokal ---
    let classifier;
    analyzeButton.addEventListener('click', async () => {
        const text = sentimentInput.value;
        if (!text) return;

        sentimentResult.textContent = 'Menganalisis...';
        speakText('Sedang menganalisis teks Anda.'); // Chika berbicara saat menganalisis

        // Inisialisasi pengklasifikasi saat mengklik untuk pertama kalinya
        if (!classifier) {
            try {
                classifier = await pipeline('sentiment-analysis');
            } catch (error) {
                console.error('Pemuatan model gagal:', error);
                sentimentResult.textContent = 'Maaf, pemuatan model gagal.';
                speakText('Maaf, pemuatan model gagal.'); // Chika berbicara pesan error
                return;
            }
        }

        // Lakukan analisis sentimen
        try {
            const result = await classifier(text);
            // Menampilkan emosi dan skor yang paling umum
            const primaryEmotion = result[0];
            sentimentResult.textContent = `suasana hati: ${primaryEmotion.label}, Pecahan: ${primaryEmotion.score.toFixed(2)}`;

            let ttsResponse = '';
            if (primaryEmotion.label === 'POSITIVE') {
                ttsResponse = 'Teks Anda terdengar positif!';
            } else if (primaryEmotion.label === 'NEGATIVE') {
                ttsResponse = 'Teks Anda terdengar negatif.';
            } else {
                ttsResponse = 'Teks Anda terdengar netral.';
            }
            speakText(ttsResponse); // Chika berbicara hasil analisis
        } catch (error) {
            console.error('Analisis sentimen gagal:', error);
            sentimentResult.textContent = 'Terjadi kesalahan selama analisis.';
            speakText('Terjadi kesalahan selama analisis.'); // Chika berbicara pesan error
        }
    });


    // --- Pengenalan ucapan lokal --- //
    const localMicButton = document.getElementById('local-mic-button');
    const localAsrResult = document.getElementById('local-asr-result');

    let recognizer = null;
    let mediaRecorder = null;
    let isRecording = false;

    const handleRecord = async () => {
        // Peralihan status: Jika perekaman sedang berlangsung, hentikan
        if (isRecording) {
            mediaRecorder.stop();
            isRecording = false;
            localMicButton.textContent = 'Mulai suara lokal';
            localMicButton.classList.remove('recording');
            return;
        }

        // Inisialisasi model (hanya sekali)
        if (!recognizer) {
            localAsrResult.textContent = 'Memuat model pengenalan suara...';
            speakText('Memuat model pengenalan suara.'); // Chika berbicara saat memuat model
            try {
                recognizer = await pipeline('automatic-speech-recognition', 'Xenova/whisper-tiny');
                localAsrResult.textContent = 'Model sudah dimuat, silakan mulai berbicara...';
                speakText('Model sudah dimuat, silakan mulai berbicara.'); // Chika berbicara saat siap
            } catch (error) {
                console.error('Pemuatan model gagal:', error);
                localAsrResult.textContent = 'Maaf, pemuatan model gagal。';
                speakText('Maaf, pemuatan model pengenalan suara gagal.'); // Chika berbicara pesan error
                return;
            }
        }

        // Mulai merekam
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            mediaRecorder = new MediaRecorder(stream);
            const audioChunks = [];

            mediaRecorder.addEventListener("dataavailable", event => {
                audioChunks.push(event.data);
            });

            mediaRecorder.addEventListener("stop", async () => {
                const audioBlob = new Blob(audioChunks, { type: mediaRecorder.mimeType });
                const arrayBuffer = await audioBlob.arrayBuffer();
                const audioContext = new (window.AudioContext || window.webkitAudioContext)();
                
                // Periksa apakah data audio kosong
                if (arrayBuffer.byteLength === 0) {
                    localAsrResult.textContent = 'Tidak ada audio yang terekam. Silakan coba lagi。';
                    speakText('Tidak ada audio yang terekam. Silakan coba lagi.'); // Chika berbicara pesan error
                    return;
                }

                try {
                    const audioBuffer = await audioContext.decodeAudioData(arrayBuffer);
                    const rawAudio = audioBuffer.getChannelData(0);
    
                    localAsrResult.textContent = 'Mengidentifikasi...';
                    speakText('Mengidentifikasi ucapan Anda.'); // Chika berbicara saat mengidentifikasi
                    const output = await recognizer(rawAudio);
                    
                    const finalTranscript = output.text || 'Tidak ada konten yang teridentifikasi.';
                    localAsrResult.textContent = finalTranscript;
                    await chikaRespondWithLLM(finalTranscript); // 🚀 Respons dari LLM

                    
                    // localAsrResult.textContent = output.text || 'Tidak ada konten yang teridentifikasi。';
                    // speakText(output.text || 'Tidak ada konten yang teridentifikasi.'); // Chika berbicara hasil identifikasi
                
                } catch(e) {
                    console.error('Dekoding atau pengenalan audio gagal:', e);
                    localAsrResult.textContent = 'Terjadi kesalahan saat memproses audio. Silakan coba lagi.。';
                    speakText('Terjadi kesalahan saat memproses audio. Silakan coba lagi.'); // Chika berbicara pesan error
                }
            });

            mediaRecorder.start();
            isRecording = true;
            localMicButton.textContent = 'Merekam... Klik untuk berhenti';
            localMicButton.classList.add('recording');

        } catch (error) {
            console.error('Pengenalan ucapan gagal:', error);
            localAsrResult.textContent = 'Tidak dapat mengakses mikrofon atau kesalahan pengenalan。';
            speakText('Tidak dapat mengakses mikrofon atau terjadi kesalahan pengenalan.'); // Chika berbicara pesan error
            isRecording = false; // Atur ulang status
            localMicButton.textContent = 'Mulai suara lokal';
            localMicButton.classList.remove('recording');
        }
    };

    localMicButton.addEventListener('click', handleRecord);

});

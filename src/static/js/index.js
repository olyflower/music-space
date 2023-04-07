let mainAudio = document.querySelector(`.main-audio`);
let currentId = 0;
let play = false;
let isChanging = false;

let slider = document.querySelector('.player__controls__timeline__slider');
let audio = document.querySelector('.audio');

function playTrack (id) {
	currentId = id;
	mainAudio.pause();
	mainAudio.currentTime = 0;
	mainAudio.querySelector('source').src = queue[currentId][0];
	mainAudio.load();
	mainAudio.play();
	play = true;
	document.querySelector('.player__controls__buttons__play').style.background = `url({% static 'pause.svg' %})`;
	document.querySelector('.player__controls__buttons__play').style.backgroundSize = `100% 100%`;
	document.querySelector('.player__info__title').innerText = queue[currentId][1];
	document.querySelector('.player__info__artist').innerText = queue[currentId][2];
}

document.querySelector('.player__controls__buttons__previous').addEventListener('click', () => {
	playTrack(--currentId);
});

document.querySelector('.player__controls__buttons__play').addEventListener('click', () => {
	if (play) {
		mainAudio.pause();
		document.querySelector('.player__controls__buttons__play').style.background = `url({% static 'pause.svg' %})`;
	} else {
		mainAudio.play();
		document.querySelector('.player__controls__buttons__play').style.background = `url({% static 'play.svg' %})`;
	}
	play = !play;
	document.querySelector('.player__controls__buttons__play').style.backgroundSize = `100% 100%`;
});

document.querySelector('.player__controls__buttons__next').addEventListener('click', () => {
	playTrack(++currentId);
});

setInterval(() => {
	if (isChanging) return;
	console.log('+');
	slider.max = Math.ceil(mainAudio.duration ? mainAudio.duration : '00:00');
	slider.value = parseInt(mainAudio.currentTime);
	slider.setAttribute('value', parseInt(mainAudio.currentTime));
	document.querySelector('.player__controls__timeline__start').innerText = mainAudio.duration ? Math.floor(mainAudio.currentTime / 60) + ':' + Math.ceil(mainAudio.currentTime % 60).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping: false }) : '00:00';
	document.querySelector('.player__controls__timeline__end').innerText =  mainAudio.duration ? Math.floor(mainAudio.duration / 60) + ':' + Math.ceil(mainAudio.duration % 60).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping: false }) : '00:00';
}, 1000);

slider.addEventListener('mousedown', (e) => {
	isChanging = true;
	e.preventDefault();
});

slider.addEventListener('mouseup', () => {
	isChanging = false;
});

slider.addEventListener('change', () => {
	mainAudio.currentTime = slider.value;
});

document.querySelector('.player__volume__slider').addEventListener('input', () => {
	mainAudio.volume = +document.querySelector('.player__volume__slider').value;
});

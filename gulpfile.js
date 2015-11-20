var gulp = require('gulp');
var sass = require('gulp-sass');

var config = {
    bootstrapDir: './lib/bootstrap-sass',
    mainDir: './templates',
};

gulp.task('css', function() {
    return gulp.src(config.mainDir + '/sass/app.scss')
    .pipe(sass({
        includePaths: [config.bootstrapDir + '/assets/stylesheets'],
    }))
    .pipe(gulp.dest(config.mainDir + '/css'));
});

gulp.task('fonts', function() {
    return gulp.src(config.bootstrapDir + '/assets/fonts/**/*')
    .pipe(gulp.dest(config.mainDir + '/fonts'));
});

gulp.task('default', ['css', 'fonts']);
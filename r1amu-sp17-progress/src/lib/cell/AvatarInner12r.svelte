<script>
    let className;
    export { className as class };
</script>

<div class="c {className}">
    <slot />
</div>

<style lang="postcss" module>
    .c {
        @apply block aspect-square overflow-hidden /**avatar > div*/ 
        w-12 rounded;
    }
</style>
